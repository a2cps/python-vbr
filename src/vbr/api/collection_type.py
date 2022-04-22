from vbr.tableclasses import CollectionType

__all__ = ["CollectionTypeApi"]


class CollectionTypeApi(object):
    def get_collection_type(self, pkid: str) -> CollectionType:
        """Retrieve a CollectionType by primary identifier."""
        return self._get_row_from_table_with_id("collection_type", pkid)

    def get_collection_type_by_local_id(self, local_id: str) -> CollectionType:
        """Retrieve a CollectionType by local_id."""
        return self._get_row_from_table_with_local_id("collection_type", local_id)
