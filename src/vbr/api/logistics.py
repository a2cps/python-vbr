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
                           container: Container,
                           location: Location,
                           sync: bool = True) -> Container:
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

    def _sync_container_location_with_parent(
            self, container: Container) -> Container:
        """Synchronize locations of a Container with its parent."""
        parent = self.get_container_parent(container)
        container.location = parent.location
        # TODO - relocated data event?
        return self.vbr_client.update_row(container)

    def attach_container_to_parent(self,
                                   container: Container,
                                   parent: Container,
                                   sync: bool = True) -> Container:
        """Attach a Container to a parent Container."""
        container.parent_container_id = parent.container_id
        container = self.vbr_client.update_row(container)
        if sync:
            container = self._sync_container_location_with_parent(container)
        return container

    def detach_container_from_parent(self, container: Container) -> Container:
        """Detach a Container from a parent Container."""
        # if container is None:
        #     container = self.get_container(container_id)
        # 0 is the system base container
        container.parent_container_id = 0
        return self.vbr_client.update_row(container)

    def get_container_parent(self, container: Container) -> Container:
        """Retrieve parent Container of a Container."""
        # if container is None:
        #     container = self.get_container(container_id)
        if container.parent_container_id is None:
            return None
        else:
            return self.get_container(container.parent_container_id)

    def get_container_children(self, container: Container) -> list:
        """Retrieve child Containers for a Container."""
        query = {
            'parent_container_id': {
                'operator': '=',
                'value': container.container_id
            }
        }
        return self.vbr_client.query_rows(root_url='container', query=query)
