from .config import Config

__all__ = ['ForeignKey']

ON_EVENT_ALLOWED = ['ON DELETE', 'ON UPDATE']
EVENT_ACTION_ALLOWED = [
    'CASCADE', 'SET_NULL', 'SET DEFAULT', 'RESTRICT', 'NO ACTION'
]


class ForeignKey(object):
    def __init__(self, source, on_event='ON DELETE', event_action='CASCADE'):
        self.foreign_key = True
        (self.reference_table, self.reference_column) = source.split('.')

        self.on_event = on_event.upper()
        if self.on_event not in ON_EVENT_ALLOWED:
            raise ValueError('Invalid value for on_event')
        self.event_action = event_action.upper()
        if self.event_action not in EVENT_ACTION_ALLOWED:
            raise ValueError('Invalid value for event_action')

    def properties(self):

        return {
            'foreign_key': self.foreign_key,
            'reference_table': self.reference_table,
            'reference_column': self.reference_column,
            'on_event': self.on_event,
            'event_action': self.event_action
        }
