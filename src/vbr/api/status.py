from vbr.tableclasses import Status

__all__ = ["StatusApi"]


class StatusApi(object):
    def get_status(self, pkid: str) -> Status:
        """Retrieve a Status by primary identifier."""
        return self._get_row_from_table_with_id("status", pkid)

    def get_status_by_name(self, name: str) -> Status:
        """Retrieve a Status by name."""
        query = {"name": {"operator": "=", "value": name}}
        return self.vbr_client.query_rows(root_url="status", query=query)[0]
