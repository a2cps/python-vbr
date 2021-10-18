from vbr.tableclasses import (Biosample, Container, Location, Measurement,
                              Project, Subject)
from .biosample import BiosampleApi
from .container import ContainerApi
from .location import LocationApi
from .measurement import MeasurementApi
from .project import ProjectApi
from .subject import SubjectApi

__all__ = ['CompositeApi']


class CompositeApi(object):
    """Supports queries and actions spanning VBR types.
    """
    def get_measurements_in_biosample(self,
                                      local_id: str = None,
                                      biosample_id: int = None) -> list:
        """Retrieve Measurements derived from a Biosample."""
        raise NotImplemented()

    def get_measurements_in_container(self,
                                      local_id: str = None,
                                      container_id: int = None) -> list:
        """Retrieve Measurements in a Container."""
        raise NotImplemented()

    def relocate_container(self,
                           local_id: str,
                           location_local_id: str = None,
                           location_id: int = None) -> Container:
        """Move a Container to a new Location."""
        # TODO Create and link a 'relocate' data_event
        # TODO Account for ContainerInContainer relationships
        if location_id is None and location_local_id is None:
            raise ValueError(
                'Either location_id or location_local_id must be provided')
        if location_id is not None:
            loc = LocationApi.get_location(self, location_id)
        else:
            loc = LocationApi.get_location_by_local_id(location_local_id)
        cont = ContainerApi.get_container_by_local_id(local_id)
        cont.location = loc.location_id
        cont = self.vbr_client.update_row(cont)
        return cont

    def relocate_measurement(self, local_id: str,
                             container_local_id: str) -> Measurement:
        """Move a Measurement to a new Container."""
        # 4. TODO Create and link a 'relocate' data_event
        meas = Measurement.get_measurement_by_local_id(self, local_id)
        cont = ContainerApi.get_container_by_local_id(self, container_local_id)
        meas.container = cont.container_id
        meas = self.vbr_client.update_row(meas)
        return meas
