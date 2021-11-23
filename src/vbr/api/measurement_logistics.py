import copy
from re import M

from vbr.pgrest.time import timestamp
from vbr.tableclasses import (Biosample, Container, ContainerInShipment,
                              Location, Measurement, Project, Shipment,
                              Subject)
from vbr.tableclasses.single_tables import MeasurementType
from vbr.utils import utc_time_in_seconds

from .container import ContainerApi
from .data_event import DataEventApi
from .measurement import MeasurementApi

__all__ = ["MeasurementLogisticsApi"]


# Methods defined here focus on Measurement handling logistics
# and tend to span multiple VBR types
class MeasurementLogisticsApi(object):
    def relocate_measurement(
        self, measurement: Measurement, container: Container, comment: str = None
    ) -> Measurement:
        """Move a Measurement to a Container."""
        orig_measurement_container = measurement.container
        measurement.container = container.container_id
        container = self.vbr_client.update_row(measurement)
        DataEventApi.create_and_link(
            self,
            comment="Relocated to container {0}".format(container.local_id),
            link_target=measurement,
        )
        return measurement

    def rebox_measurement_by_local_id(
        self, local_id: str, container_local_id: str, comment: str = None
    ) -> Measurement:
        """Move a Measurement to a Container by local_ids."""
        meas = MeasurementApi.get_measurement_by_local_id(self, local_id)
        cont = ContainerApi.get_container_by_local_id(self, container_local_id)
        return self.relocate_measurement(meas, cont, comment)

    def get_measurements_in_container(self, container: Container) -> list:
        """Retrieve Measurements in a Container."""
        query = {"container": {"operator": "=", "value": container.container_id}}
        return self.vbr_client.query_rows(root_url="measurement", query=query)

    def get_measurements_in_biosample(self, biosample: Biosample) -> list:
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

    def get_measurement_partitions(self, measurement: Measurement) -> list:
        """Retrieve Measurements partioned from a Measurment."""
        # Query MeasurementFromMeasurement table
        raise NotImplemented()
