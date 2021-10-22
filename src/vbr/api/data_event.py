from vbr.tableclasses import DataEvent, Table, AssociationTable
from vbr.tableclasses import class_from_table
from vbr.errors import TableNotSupported

__all__ = ['DataEventApi']

# protocol_id:int
# reason_id:int
# status_id:int
# performed_by_id:int
# event_ts_str:str
# rank:int
# comment:str


class DataEventApi(object):
    def create_data_event(self,
                          protocol_id: int = None,
                          reason_id: int = None,
                          status_id: int = None,
                          performed_by_id: int = None,
                          event_ts_str: str = None,
                          rank: int = None,
                          comment: str = None) -> DataEvent:
        """Create a new DataEvent with supplied kwargs."""
        de = DataEvent(protocol=protocol_id,
                       reason=reason_id,
                       status=status_id,
                       perfomed_by=performed_by_id,
                       event_ts=event_ts_str,
                       rank=rank,
                       comment=comment)
        try:
            return self.vbr_client.create_row(de)[0]
        except Exception:
            raise

    def link_data_event(self,
                        data_event: DataEvent,
                        link_target: Table = None) -> AssociationTable:
        """Link a DataEvent with another VBR Table entity via an AssociationTable."""

        # Return an empty AssociationTable if no link_target specified
        if link_target is None:
            return AssociationTable()

        # Look up the relevant AssocationTable class
        left_table_name = 'data_event'
        left_table_id_name = 'data_event_id'
        left_table_id_value = getattr(data_event, left_table_id_name)

        right_table_name = link_target.__schema__.root_url
        right_table_id_name = right_table_name + '_id'
        right_table_id_value = getattr(link_target, right_table_id_name)

        combined_table_name = '{0}_in_{1}'.format(left_table_name,
                                                  right_table_name)

        try:
            table_class = class_from_table(combined_table_name)
        except TableNotSupported:
            raise TableNotSupported(
                'Unable to link {0} to a data_event'.format(right_table_name))
        except Exception:
            raise

        # Create a DataEventIn<Class> entry
        data = {
            left_table_name: left_table_id_value,
            right_table_name: right_table_id_value
        }
        de = table_class(**data)
        try:
            return self.vbr_client.create_row(de)[0]
        except Exception:
            raise

    def create_and_link(self,
                        protocol_id: int = None,
                        reason_id: int = None,
                        status_id: int = None,
                        performed_by_id: int = None,
                        event_ts_str: str = None,
                        rank: int = None,
                        comment: str = None,
                        link_target: Table = None) -> tuple:

        data_event = self.create_data_event(protocol_id, reason_id, status_id,
                                            performed_by_id, event_ts_str,
                                            rank, comment)
        association = self.link_data_event(data_event, link_target=link_target)

        return (data_event, association)
