from vbr.tableclasses import Container

__all__ = ['ContainerApi']


class ContainerApi(object):
    def get_container(self, pkid: str) -> Container:
        """Retrieve a Container by primary identifier."""
        return self._get_row_from_table_with_id('container', pkid)

    def get_container_by_local_id(self, local_id: str) -> Container:
        """Retrieve a Container by local_id."""
        return self._get_row_from_table_with_local_id('container', local_id)

    def get_container_by_tracking_id(self, tracking_id: str) -> Container:
        """Retrieve a Container by tracking_id."""
        return self._get_row_from_table_with_tracking_id(
            'container', tracking_id)

    def relabel_container_by_local_id(self, local_id: str,
                                      new_tracking_id: str) -> Container:
        """Update the tracking_id for a Container by local_id."""
        # 1. Query for row matching local_id
        # 2. Set the new value
        # 3. Do database update via vbr_client.update_row()
        # 4. TODO Create and link a 'rename' data_event
        cont = self.get_biosample_by_local_id(local_id)
        cont.tracking_id = new_tracking_id
        cont = self.vbr_client.update_row(cont)
        return cont

    # TODO Update status

    def create_container(self,
                         tracking_id: str,
                         project_id: int,
                         container_type_id: int,
                         location_id: int = 1) -> Container:
        """Create a new Container."""
        container_type_id = str(container_type_id)
        location_id = str(location_id)
        ct = Container(tracking_id=tracking_id,
                       container_type=container_type_id,
                       location=location_id)
        try:
            return self.vbr_client.create_row(ct)[0]
        except Exception:
            raise

    def create_or_get_container_by_tracking_id(
            self,
            tracking_id: str,
            project_id: int,
            container_type_id: int,
            location_id: int = 1) -> Container:
        """Create a Container or return existing with specified tracking_id."""
        try:
            return self.create_container(tracking_id, project_id,
                                         container_type_id, location_id)
        except Exception:
            return self.get_container_by_tracking_id(tracking_id)
