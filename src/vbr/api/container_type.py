from vbr.tableclasses import ContainerType

__all__ = ["ContainerTypeApi"]


class ContainerTypeApi(object):
    def get_container_type(self, pkid: str) -> ContainerType:
        """Retrieve a ContainerType by primary identifier."""
        return self._get_row_from_table_with_id("container_type", pkid)

    def get_container_type_by_local_id(self, local_id: str) -> ContainerType:
        """Retrieve a ContainerType by local_id."""
        return self._get_row_from_table_with_local_id("container_type", local_id)
