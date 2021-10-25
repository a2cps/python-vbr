import copy
from vbr.tableclasses import (Biosample, Container, Location, Measurement,
                              Project, Shipment, Subject)
from vbr.tableclasses import (ContainerInShipment)
from vbr.utils import utc_time_in_seconds

from .biosample import BiosampleApi
from .container import ContainerApi
from .location import LocationApi
from .measurement import MeasurementApi
from .project import ProjectApi
from .subject import SubjectApi

__all__ = ['MeasurementLogisticsApi']


# Methods defined here focus on Measurement handling logistics
# and tend to span multiple VBR types
class MeasurementLogisticsApi(object):
    def relocate_measurement(self, measurement: Measurement,
                             container: Container) -> Measurement:
        """Move a Measurement to a Container."""
        # 4. TODO Create and link a 'relocate' data_event
        measurement.container = container.container_id
        container = self.vbr_client.update_row(measurement)
        return measurement

    def get_measurements_in_container(self, container: Container) -> list:
        """Retrieve Measurements in a Container."""
        query = {
            'container': {
                'operator': '=',
                'value': container.container_id
            }
        }
        return self.vbr_client.query_rows(root_url='measurement', query=query)

    def get_measurements_in_biosample(self, biosample: Biosample) -> list:
        """Retrieve Measurements in a Biosample."""
        query = {
            'biosample': {
                'operator': '=',
                'value': biosample.biosample_id
            }
        }
        return self.vbr_client.query_rows(root_url='measurement',
                                          query=query,
                                          limit=1000000)

    def partition_measurement(self,
                              measurement: Measurement,
                              tracking_id: str = None) -> Measurement:
        """Partition a sub-Measuremenent from a Measurement."""
        # 1. Clone the original Measurement to a new Measurement,
        # appending date in seconds to tracking_id if one is not provided
        m2 = measurement.clone()
        m2.measurement_id = None
        m2.local_id = None
        m2.creation_time = None
        if tracking_id is not None:
            m2.tracking_id = tracking_id
        else:
            m2.tracking_id = measurement.tracking_id + '.' + utc_time_in_seconds(
            )
        m2 = self.vbr_client.create_row(m2)[0]
        # 2. Register the relation via MeasurementFromMeasurement table
        # 3. Create a partitioned data event for original Measurement
        # 4. Return new Measurement
        return m2

    def get_measurement_partitions(self, measurement: Measurement) -> list:
        """Retrieve Measurements partioned from a Measurment."""
        # Query MeasurementFromMeasurement table
        raise NotImplemented()
