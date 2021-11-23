from vbr.tableclasses import Location

__all__ = ["LocationApi"]


class LocationApi(object):
    def get_location(self, pkid: str) -> Location:
        """Retrieve a Location by primary identifier."""
        return self._get_row_from_table_with_id("location", pkid)

    def get_location_by_local_id(self, local_id: str) -> Location:
        """Retrieve a Location by local_id."""
        return self._get_row_from_table_with_local_id("location", local_id)
