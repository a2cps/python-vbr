from vbr.tableclasses import (Biosample, Container, Location, Measurement,
                              Project, Subject)
from .biosample import BiosampleApi
from .container import ContainerApi
from .location import LocationApi
from .measurement import MeasurementApi
from .project import ProjectApi
from .subject import SubjectApi

__all__ = ['LogisticsApi']


# Methods defined here focus on sample and container handling logistics
# and tend to span multiple VBR types
class LogisticsApi(object):
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

    def relocate_measurement(self, local_id: str,
                             container_local_id: str) -> Measurement:
        """Move a Measurement to a Container."""
        # 4. TODO Create and link a 'relocate' data_event
        meas = Measurement.get_measurement_by_local_id(self, local_id)
        cont = ContainerApi.get_container_by_local_id(self, container_local_id)
        meas.container = cont.container_id
        meas = self.vbr_client.update_row(meas)
        return meas

    def relocate_container(self,
                           local_id: str,
                           location_local_id: str = None,
                           location_id: int = None) -> Container:
        """Move a Container to a Location."""
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
        # TODO - relocated data event?
        cont = self.vbr_client.update_row(cont)
        return cont

    def _sync_child_container_locations(self, container: Container) -> None:
        # Iterate thru get_container_children(container) setting location
        # for each to its parent
        # TODO - Make this recursive. Probably good enough for now
        for child in self.get_container_children(container):
            child.location = container.location
            # TODO - relocated data event?
            self.vbr_client.update_row(child)

    def attach_container_to_parent(
            self,
            container: Container = None,
            container_id: int = None,
            container_parent: Container = None,
            container_parent_id: int = None) -> Container:
        """Attach a Container to a parent Container."""
        if container is None:
            container = self.get_container(container_id)
        if container_parent is None:
            container_parent = self.get_container(container_parent_id)
        container.parent_id = container_parent.container_id
        return self.vbr_client.update_row(container)

    def detach_container_from_parent(self,
                                     container: Container = None,
                                     container_id: int = None) -> Container:
        """Detach a Container from its parent Container."""
        if container is None:
            container = self.get_container(container_id)
        container.parent_id = None
        return self.vbr_client.update_row(container)

    def get_container_parent(self,
                             container: Container = None,
                             container_id: int = None) -> Container:
        """Retrieve parent Container of a Container."""
        if container is None:
            container = self.get_container(container_id)
        if container.parent_container_id is None:
            return None
        else:
            return self.get_container(container.parent_container_id)

    def get_container_children(self,
                               container: Container = None,
                               container_id: int = None) -> list:
        """Retrieve child Containers for a Container."""
        if container is not None:
            query = {
                'parent_container_id': {
                    'operator': '=',
                    'value': container.container_id
                }
            }
        elif container_id is not None:
            query = {
                'parent_container_id': {
                    'operator': '=',
                    'value': str(container_id)
                }
            }
        else:
            raise ValueError(
                'Either a Container object or container_id must be provided.')
        return self.vbr_client.query_rows(root_url='container', query=query)
