from vbr.tableclasses import ContainerType

__all__ = ["ContainerTypeApi"]


class ContainerTypeApi(object):
    def get_container_type(self, pkid: str) -> ContainerType:
        """Retrieve a ContainerType by primary identifier."""
        return self._get_row_from_table_with_id("container_type", pkid)

    def get_container_type_by_local_id(self, local_id: str) -> ContainerType:
        """Retrieve a ContainerType by local_id."""
        return self._get_row_from_table_with_local_id("container_type", local_id)

    def create_container_type(
        self, name: str, description: str = None
    ) -> ContainerType:
        """Create a new ContainerType."""
        # TODO - Add a data_event marking the creation
        ct = ContainerType(name=name, description=description)
        try:
            return self.vbr_client.create_row(ct)[0]
        except Exception:
            raise
