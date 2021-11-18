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

from .container import ContainerApi
from .data_event import DataEventApi
from .location import LocationApi
from .status import StatusApi

# from .biosample import BiosampleApi
# from .measurement import MeasurementApi
# from .project import ProjectApi
# from .subject import SubjectApi

__all__ = ["ContainerLogisticsApi"]


# Methods defined here focus on Container handling logistics
# and tend to span multiple VBR types
class ContainerLogisticsApi(object):
    def relocate_container_by_local_id(
        self, local_id: str, location_local_id: str, comment: str = None
    ) -> Measurement:
        """Move a Container to new Location by local_ids."""
        cont = ContainerApi.get_container_by_local_id(self, local_id)
        loca = LocationApi.get_location_by_local_id(self, location_local_id)
        return self.relocate_container(cont, loca, comment)

    def relocate_container(
        self,
        container: Container,
        location: Location,
        sync: bool = True,
        comment: str = None,
    ) -> Container:
        """Move a Container to a Location."""
        if container.container_id == 0:
            raise ValueError("Cannot relocate default container")
        container.location = location.location_id
        container = self.vbr_client.update_row(container)
        if sync:
            self._sync_child_container_locations(container)
        return container

    def _sync_child_container_locations(self, container: Container) -> None:
        """Synchronize locations of child Containers with their parent [recursive]."""
        # Iterate thru get_container_children(container) setting location
        # for each to its parent
        if container.container_id == 0:
            raise ValueError("Cannot sync children of the default container")
        for child in self.get_container_children(container):
            child.location = container.location
            # TODO - relocated data event?
            self.vbr_client.update_row(child)

    def _sync_container_location_with_parent(self, container: Container) -> Container:
        """Synchronize locations of a Container with its parent."""
        if container.container_id == 0:
            raise ValueError("Cannot sync default container with a parent")
        parent = self.get_container_parent(container)
        container.location = parent.location
        # TODO - relocated data event?
        return self.vbr_client.update_row(container)

    def put_container_in_container(
        self, container: Container, parent: Container, sync: bool = True
    ) -> Container:
        """Put a Container inside a parent Container."""
        if container.container_id == 0:
            raise ValueError("Cannot nest root container in another")
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

    def get_container_lineage(self, container: Container, lineage=None) -> list:
        """Retrieve a Container's complete parental lineage [recursive].

        Returns a list in order [container,parent....,root]"""
        if lineage is None:
            lineage = []
            lineage.append(container)
        parent = self.get_container(container.parent_container)
        if (
            parent.parent_container is not None
            and parent.parent_container != container.container_id
            and container.container_id != 0
        ):
            lineage.append(parent)
            self.get_container_lineage(parent, lineage)
        return lineage

    def get_container_parents(self, container: Container) -> list:
        """Retrieve a Container's parental lineage [recursive].

        Returns a list in order [parent....,root]"""
        return self.get_container_lineage(container)[1:]

    def get_container_children(self, container: Container, descendants=None) -> list:
        # TODO - check this with branching relations
        """Retrieve child Containers [recursive]."""
        if container.container_id == 0:
            raise ValueError("Cannot get children for root container")
        if descendants is None:
            descendants = []
        query = {"parent_container": {"operator": "=", "value": container.container_id}}
        kids = self.vbr_client.query_rows(root_url="container", query=query)
        descendants.extend(kids)
        if len(kids) > 0:
            for kid in kids:
                self.get_container_children(kid, descendants=descendants)
        return descendants

    def _get_shipment_for_container(self, container: Container) -> Shipment:
        """Retrieve the Shipment for a container [recursive]."""
        query = {"container": {"operator": "=", "value": container.container_id}}
        try:
            c_in_s = self._get_row_from_table_with_query("container_in_shipment", query)
            return self._get_row_from_table_with_id("shipment", c_in_s.shipment)
        except ValueError:
            return None

    def get_shipment_for_container(self, container: Container) -> Shipment:
        """Retrieve the Shipment for a container [recursive]."""
        # Walk up lineage, startng with provided container, attempting to
        # return a shipment associated with the container. This allows
        # a container to inherit a shipment from its parent.
        #
        # We drop the terminal container as it is always assumed to be
        # the root container
        container_lineage = self.get_container_lineage(container)[:-1]
        for container in container_lineage:
            query = {"container": {"operator": "=", "value": container.container_id}}
            try:
                c_in_s = self._get_row_from_table_with_query(
                    "container_in_shipment", query
                )
                return self._get_row_from_table_with_id("shipment", c_in_s.shipment)
            except ValueError:
                pass
        return None

    def get_containers_for_shipment(self, shipment: Shipment) -> list:
        """Retrieve Container(s) in Shipment [non-recursive]."""
        query = {"shipment": {"operator": "=", "value": shipment.shipment_id}}
        try:
            conts = []
            c_in_s = self._get_row_from_table_with_query("container_in_shipment", query)
            conts.append(
                self._get_row_from_table_with_id("container", c_in_s.container)
            )
            return conts
        except ValueError:
            return []

    # TODO - DataEvent
    def associate_container_with_shipment(
        self, container: Container, shipment: Shipment, sync: bool = True
    ) -> ContainerInShipment:
        """Associate a Container with a Shipment."""
        conshp = ContainerInShipment(
            container=container.container_id, shipment=shipment.shipment_id
        )
        try:
            resp = self.vbr_client.create_row(conshp)
            return resp
        except Exception:
            query = {
                "container": {"operator": "=", "value": container.container_id},
                "shipment": {"operator": "=", "value": shipment.shipment_id},
            }
            if (
                len(
                    self._get_rows_from_table_with_query("container_in_shipment", query)
                )
                > 0
            ):
                # Already attached
                pass
            else:
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
