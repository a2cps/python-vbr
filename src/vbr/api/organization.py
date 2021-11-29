from vbr.tableclasses import Organization

__all__ = ["OrganizationApi"]


class OrganizationApi(object):
    def get_organization(self, pkid: str) -> Organization:
        """Retrieve a Organization by primary identifier."""
        return self._get_row_from_table_with_id("organization", pkid)

    def get_organization_by_name(self, name: str) -> Organization:
        """Retrieve a Organization by name."""
        query = {"name": {"operator": "=", "value": name}}
        return self._get_row_from_table_with_query("organization", query)
