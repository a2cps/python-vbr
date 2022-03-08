from vbr.tableclasses import Collection

__all__ = ["CollectionApi"]


class CollectionApi(object):
    def get_collection(self, pkid: str) -> Collection:
        """Retrieve a Collection by primary identifier."""
        return self._get_row_from_table_with_id("collection", pkid)

    def get_collection_by_local_id(self, local_id: str) -> Collection:
        """Retrieve a Collection by local_id."""
        return self._get_row_from_table_with_local_id("collection", local_id)

    def get_collection_by_tracking_id(self, tracking_id: str) -> None:
        """Retrieve a Collection by tracking_id."""
        return self._get_row_from_table_with_tracking_id("collection", tracking_id)

    def create_collection(
        self,
        name: str,
        description: str,
        tracking_id: str,
        status_id: int = 10,  # created
        collection_type_id: int = 1,  # default to 1 -> run list
    ) -> Collection:
        """Create a new Collection."""
        collection_type_id = str(collection_type_id)
        location_id = str(location_id)
        ct = Collection(
            tracking_id=tracking_id,
            collection_type=collection_type_id,
            name=name,
            description=description,
        )
        try:
            return self.vbr_client.create_row(ct)[0]
        except Exception:
            raise

    def create_or_get_collection_by_tracking_id(
        self,
        name: str,
        description: str,
        tracking_id: str,
        status_id: int = 10,
        collection_type_id: int = 1,
    ) -> Collection:
        """Create a Collection or return existing with specified tracking_id."""
        try:
            return self.create_collection(
                name, description, tracking_id, status_id, collection_type_id
            )
        except Exception:
            return self.get_collection_by_tracking_id(tracking_id)
