from vbr.tableclasses import CollectionType

__all__ = ["CollectionTypeApi"]


class CollectionTypeApi(object):
    def get_collection_type(self, pkid: str) -> CollectionType:
        """Retrieve a CollectionType by primary identifier."""
        return self._get_row_from_table_with_id("collection_type", pkid)

    def get_collection_type_by_local_id(self, local_id: str) -> CollectionType:
        """Retrieve a CollectionType by local_id."""
        return self._get_row_from_table_with_local_id("collection_type", local_id)

    def create_collection_type(
        self, name: str, description: str = None
    ) -> CollectionType:
        """Create a new CollectionType."""
        # TODO - Add a data_event marking the creation
        ct = CollectionType(name=name, description=description)
        try:
            return self.vbr_client.create_row(ct)[0]
        except Exception:
            raise
