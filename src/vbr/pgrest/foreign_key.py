from .config import Config

__all__ = ['ForeignKey']

ON_EVENT_ALLOWED = ['ON DELETE', 'ON UPDATE']
EVENT_ACTION_ALLOWED = [
    'CASCADE', 'SET_NULL', 'SET DEFAULT', 'RESTRICT', 'NO ACTION'
]


class ForeignKey(object):
    def __init__(self, source, on_event='ON DELETE', event_action='RESTRICT'):
        self.foreign_key = True
        (self.reference_table, self.reference_column) = source.split('.')
        self.on_event = None
        self.event_action = None

        if on_event:
            on_event = on_event.upper()
            if on_event not in ON_EVENT_ALLOWED:
                raise ValueError(
                    'Invalid value {0} for on_event'.format(on_event))
            else:
                self.on_event = on_event

        if event_action:
            event_action = event_action.upper()
            if event_action not in EVENT_ACTION_ALLOWED:
                raise ValueError(
                    'Invalid value {0} for event_action'.format(event_action))
            else:
                self.event_action = event_action

    def properties(self):

        data = {
            'foreign_key': self.foreign_key,
            'reference_table': self.reference_table,
            'reference_column': self.reference_column
        }

        if self.on_event:
            data['on_event'] = self.on_event
        if self.event_action:
            data['event_action'] = self.event_action

        return data
