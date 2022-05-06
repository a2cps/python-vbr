from vbr.tableclasses import SysEvent

__all__ = ["SysEventApi"]


class SysEventApi(object):
    """Manage system-level Redcap events."""

    def create_vbr_redcap_event(self, **kwargs):
        """Create and store a SysEvent."""
        evt = SysEvent(**kwargs)
        print(evt)
        try:
            return self.vbr_client.create_row(evt)[0]
        except Exception:
            raise

    def get_vbr_redcap_event(self, pkid: str) -> SysEvent:
        """Retrieve a SysEvent by primary identifier."""
        return self._get_row_from_table_with_id("sys_event", pkid)

    def get_vbr_redcap_event_by_local_id(self, local_id: str) -> SysEvent:
        """Retrieve a SysEvent by local_id."""
        return self._get_row_from_table_with_local_id("sys_event", local_id)

    def set_vbr_redcap_event_status(self, event: SysEvent, status: str) -> SysEvent:
        """Update a SysEvent's status."""
        event.set_status(status)
        event = self.vbr_client.update_row(event)
        return event
