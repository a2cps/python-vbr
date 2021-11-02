from vbr.tableclasses import VbrRedcapEvent

__all__ = ['VbrRedcapEventApi']


class VbrRedcapEventApi(object):
    """Manage system-level Redcap events.
    """
    def create_vbr_redcap_event(self, **kwargs):
        """Create and store a VbrRedcapEvent.
        """
        evt = VbrRedcapEvent(**kwargs)
        print(evt)
        try:
            return self.vbr_client.create_row(evt)[0]
        except Exception:
            raise

    def get_vbr_redcap_event(self, pkid: str) -> VbrRedcapEvent:
        """Retrieve a VbrRedcapEvent by primary identifier."""
        return self._get_row_from_table_with_id('vbr_redcap_event', pkid)

    def get_vbr_redcap_event_by_local_id(self,
                                         local_id: str) -> VbrRedcapEvent:
        """Retrieve a VbrRedcapEvent by local_id."""
        return self._get_row_from_table_with_local_id('vbr_redcap_event',
                                                      local_id)

    def get_vbr_redcap_events_by_status(self, status: str) -> list:
        """Retrieve all VbrRedcapEvents with a given status."""
        query = {'event_status': {'operator': '=', 'value': status}}
        try:
            return self._get_rows_from_table_with_query(
                root_url='vbr_redcap_event', query=query)
        except Exception:
            return []

    def set_vbr_redcap_event_status(self, event: VbrRedcapEvent,
                                    status: str) -> VbrRedcapEvent:
        """Update a VbrRedcapEvent's status."""
        event.set_status(status)
        event = self.vbr_client.update_row(event)
        return event
