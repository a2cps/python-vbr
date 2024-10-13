from typing import List, NoReturn

from vbr.pgrest.time import timestamp
from vbr.tableclasses import (
    Biosample,
    Collection,
    Container,
    ContainerInShipment,
    Location,
    Measurement,
    MeasurementInCollection,
    Shipment,
)
from vbr.utils import utc_time_in_seconds

from .container import ContainerApi
from .data_event import DataEventApi
from .location import LocationApi
from .measurement import MeasurementApi

__all__ = ["LogisticsApi"]


class LogisticsApi(object):
    """APIs that involve combinations of shipments, containers, biosamples, measurements, locations, and collections"""

    def relocate_container_by_local_id(
        self, local_id: str, location_local_id: str, comment: str = None
    ) -> Container:
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

    def _sync_child_container_locations(self, container: Container) -> NoReturn:
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

    def get_container_lineage(
        self, container: Container, lineage=None
    ) -> List[Container]:
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

    def get_container_parents(self, container: Container) -> List[Container]:
        """Retrieve a Container's parental lineage [recursive].

        Returns a list in order [parent....,root]"""
        return self.get_container_lineage(container)[1:]

    def get_container_children(
        self, container: Container, recursive=True, descendants=None
    ) -> List[Container]:
        # TODO - check this with branching relations
        """Retrieve child Containers [recursive]."""
        if container.container_id == 0:
            raise ValueError("Cannot get children for root container")
        if descendants is None:
            descendants = []
        query = {"parent_container": {"operator": "=", "value": container.container_id}}
        kids = self.vbr_client.query_rows(root_url="container", query=query)
        descendants.extend(kids)
        if len(kids) > 0 and recursive is True:
            for kid in kids:
                self.get_container_children(
                    kid, recursive=recursive, descendants=descendants
                )
        return descendants

    def get_shipment_for_container(self, container: Container) -> Shipment:
        """Retrieve the Shipment for a Container [recursive]."""
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

    def get_containers_for_shipment(self, shipment: Shipment) -> List[Container]:
        """Retrieve Container(s) in Shipment [non-recursive]."""
        query = {"shipment": {"operator": "=", "value": shipment.shipment_id}}
        try:
            conts = []
            c_in_s = self._get_rows_from_table_with_query(
                "container_in_shipment", query
            )
            for rel in c_in_s:
                conts.append(
                    self._get_row_from_table_with_id("container", rel.container)
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
        # Delete existing relations
        # Container is unique in container_in_shipment
        query = {"container": {"operator": "=", "value": container.container_id}}
        try:
            rows = self._get_rows_from_table_with_query("container_in_shipment", query)
            for row in rows:
                print("Deleting", row)
                self.vbr_client.delete_row(row)
        except Exception as ex1:
            # Who cares if we can't do the delete. We can assume it's OK to create a relation below.
            pass
        try:
            resp = self.vbr_client.create_row(conshp)
            return resp
        except Exception as ex2:
            raise ValueError("Unable to attach Container to Shipment: %s", ex2)

    def disassociate_container_from_shipment(self, container: Container) -> NoReturn:
        """Disassociate a Container from its Shipment."""
        # Retrieve the relevant ContainerInShipment
        query = {"container": {"operator": "=", "value": container.container_id}}
        # Assumption is single row. Die if not!
        conshp = self._get_row_from_table_with_query("container_in_shipment", query)
        self.vbr_client.delete_row(conshp)

    def relocate_measurement(
        self, measurement: Measurement, container: Container, comment: str = None
    ) -> Measurement:
        """Move a Measurement to a Container."""
        orig_measurement_container = measurement.container
        measurement.container = container.container_id
        measurement = self.vbr_client.update_row(measurement)
        DataEventApi.create_and_link(
            self,
            comment="Relocated to container {0}".format(container.local_id),
            link_target=measurement,
        )
        return measurement

    def rebox_measurement_by_local_id(
        self, local_id: str, container_local_id: str, comment: str = None
    ) -> Measurement:
        """Move a Measurement to a Container (by local_ids)."""
        meas = MeasurementApi.get_measurement_by_local_id(self, local_id)
        cont = ContainerApi.get_container_by_local_id(self, container_local_id)
        return self.relocate_measurement(meas, cont, comment)

    def get_measurements_in_container(self, container: Container) -> List[Measurement]:
        """Retrieve Measurements in a Container."""
        query = {"container": {"operator": "=", "value": container.container_id}}
        return self.vbr_client.query_rows(root_url="measurement", query=query)

    def get_measurements_in_biosample(self, biosample: Biosample) -> List[Measurement]:
        """Retrieve Measurements in a Biosample."""
        query = {"biosample": {"operator": "=", "value": biosample.biosample_id}}
        return self.vbr_client.query_rows(
            root_url="measurement", query=query, limit=1000000
        )

    def partition_measurement(
        self, measurement: Measurement, tracking_id: str = None, comment: str = None
    ) -> Measurement:
        """Partition a sub-Measuremenent from a Measurement."""
        # 1. Clone the original Measurement to a new Measurement,
        # appending date in seconds to tracking_id if one is not provided
        m2 = measurement.clone()
        m2.measurement_id = None
        m2.local_id = None
        m2.creation_time = timestamp()
        if tracking_id is not None:
            m2.tracking_id = tracking_id
        else:
            m2.tracking_id = measurement.tracking_id + "." + utc_time_in_seconds()
        m2 = self.vbr_client.create_row(m2)[0]
        # TODO Register the relation via MeasurementFromMeasurement table
        DataEventApi.create_and_link(
            self,
            comment="Sub-aliquoted to {0}".format(m2.local_id),
            link_target=measurement,
        )
        return m2

    def get_measurement_partitions(self, measurement: Measurement) -> List[Measurement]:
        """Retrieve Measurements partioned from a Measurment."""
        # Query MeasurementFromMeasurement table
        raise NotImplemented()

    def associate_measurement_with_collection(
        self, measurement: Measurement, collection: Collection
    ) -> MeasurementInCollection:
        """Associate a Measurement with a Collection."""
        mescol = MeasurementInCollection(
            measurement=measurement.measurement_id, collection=collection.collection_id
        )
        try:
            resp = self.vbr_client.create_row(mescol)
            return resp
        except Exception as ex2:
            raise ValueError("Unable to attach Measurement to Collection: %s", ex2)

    def disassociate_measurement_from_collection(
        self, measurement: Measurement, collection: Collection
    ) -> NoReturn:
        """Disassociate a Measurement from a Collection."""
        # Retrieve the relevant MeasurementInCollection
        query = {
            "measurement": {"operator": "=", "value": measurement.measurement_id},
            "collection": {"operator": "=", "value": collection.collection_id},
        }
        # Assumption is single row. Die if not!
        mescol = self._get_row_from_table_with_query("measurement_in_collection", query)
        self.vbr_client.delete_row(mescol)
