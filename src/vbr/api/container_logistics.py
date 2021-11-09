from vbr.tableclasses import (
    Biosample,
    Container,
    ContainerInShipment,
    Location,
    Measurement,
    Project,
    Shipment,
    Status,
    Subject,
)

from .biosample import BiosampleApi
from .container import ContainerApi
from .data_event import DataEventApi
from .location import LocationApi
from .measurement import MeasurementApi
from .project import ProjectApi
from .status import StatusApi
from .subject import SubjectApi

__all__ = ["ContainerLogisticsApi"]


# Methods defined here focus on Container handling logistics
# and tend to span multiple VBR types
class ContainerLogisticsApi(object):
    def relocate_container(
        self, container: Container, location: Location, sync: bool = True
    ) -> Container:
        """Move a Container to a Location."""
        container.location = location.location_id
        container = self.vbr_client.update_row(container)
        if sync:
            self._sync_child_container_locations(container)
        return container

    def _sync_child_container_locations(self, container: Container) -> None:
        """Synchronize locations of child Containers with their parent."""
        # Iterate thru get_container_children(container) setting location
        # for each to its parent
        # TODO - Make this recursive. Probably good enough for now
        for child in self.get_container_children(container):
            child.location = container.location
            # TODO - relocated data event?
            self.vbr_client.update_row(child)

    def _sync_container_location_with_parent(self, container: Container) -> Container:
        """Synchronize locations of a Container with its parent."""
        parent = self.get_container_parent(container)
        container.location = parent.location
        # TODO - relocated data event?
        return self.vbr_client.update_row(container)

    def put_container_in_container(
        self, container: Container, parent: Container, sync: bool = True
    ) -> Container:
        """Put a Container inside a parent Container."""
        container.parent_container = parent.container_id
        container = self.vbr_client.update_row(container)
        if sync:
            container = self._sync_container_location_with_parent(container)
        return container

    def remove_container_from_parent(self, container: Container) -> Container:
        """Remove a Container from its parent Container."""
        # if container is None:
        #     container = self.get_container(container_id)
        # 0 is the system base container
        container.parent_container = 0
        return self.vbr_client.update_row(container)

    def get_container_parent(self, container: Container) -> Container:
        """Retrieve parent Container of a Container."""
        # if container is None:
        #     container = self.get_container(container_id)
        if container.parent_container is None:
            return None
        else:
            return self.get_container(container.parent_container)

    def get_container_children(self, container: Container) -> list:
        """Retrieve child Containers for a Container."""
        query = {"parent_container": {"operator": "=", "value": container.container_id}}
        return self.vbr_client.query_rows(root_url="container", query=query)

    def get_shipment_for_container(self, container: Container) -> Shipment:
        """Retrieve the Shipment (if any) for a container (not recursive)."""
        raise NotImplemented()

    # TODO - DataEvent
    def associate_container_with_shipment(
        self, container: Container, shipment: Shipment, sync: bool = True
    ) -> ContainerInShipment:
        """Associate a Container with a Shipment."""
        conshp = ContainerInShipment(
            container=container.container_id, shipment=shipment.shipment_id
        )
        # ContainerInShipment needs a constraint such that there can only be
        # one combination of container_id and shipment_id.
        try:
            resp = self.vbr_client.create_row(conshp)
            return resp
        except Exception:
            raise ValueError("Unable to attach container to shipment")

    # TODO - DataEvent
    def disassociate_container_from_shipment(self, container: Container) -> None:
        """Disassociate a Container from its Shipment."""
        # Retrieve the relevant ContainerInShipment
        query = {"container": {"operator": "=", "value": container.container_id}}
        # Assumption is single row. Die if not!
        conshp = self._get_row_from_table_with_query("container_in_shipment", query)
        self.vbr_client.delete_row(conshp)

    def set_shipment_status(
        self, shipment: Shipment, status: Status, comment: str = None
    ) -> Shipment:
        """Update Shipment status, creating a linked DataEvent in the process."""
        shipment.status = status.status_id
        shipment = self.vbr_client.update_row(shipment)
        # Create and link DataEvent
        DataEventApi.create_and_link(
            self,
            protocol_id=50,  # 50,shipping,Sample shipping
            status_id=status.status_id,  # This will be one of the easypost shipment statuses
            comment=comment,
            link_target=shipment,
        )
        return shipment

    def get_shipment_status(self, shipment: Shipment) -> Status:
        """Get current Status for a Shipment."""
        return StatusApi.get_status(self, shipment.status)

    def get_shipment_status_history(self, shipment) -> list:
        """Return list of data events for a Shipment."""
        return DataEventApi.data_events_for_record(self, record=shipment)
