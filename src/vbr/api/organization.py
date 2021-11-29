from vbr.tableclasses import Organization

__all__ = ["OrganizationApi"]


class OrganizationApi(object):
    def get_location(self, pkid: str) -> Organization:
        """Retrieve a Organization by primary identifier."""
        return self._get_row_from_table_with_id("organization", pkid)

    def get_location_by_local_id(self, local_id: str) -> Organization:
        """Retrieve a Organization by local_id."""
        return self._get_row_from_table_with_local_id("organization", local_id)
