import csv
from .constants import *

__all__ = [
    'redcap_event_to_vbr_protocol', 'redcap_event_id_to_unique_event_name'
]


def redcap_event_to_vbr_protocol(event: str) -> int:
    """Map redcap event name to VBR protocol.
    """
    # NOTE - this must be manually synced with src/scripts/data/protocol.csv
    EVENTS = {
        'informed_consent_arm_1': 2,
        'baseline_visit_arm_1': 3,
        '6wks_postop_arm1': 30,
        '3mo_postop_arm1': 31,
        'event_1_arm1': 50
    }
    return EVENTS.get(event)


def load_arms() -> dict:
    arms_data = os.path.join(os.path.dirname(__file__), 'arms.csv')
    arms = {}
    with open(arms_data, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arms[row['arm_id']] = row['arm_name']
    return arms


def load_metadata() -> dict:
    events_data = os.path.join(os.path.dirname(__file__), 'metadata.csv')
    events = {}
    with open(events_data, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            events[row['event_id']] = {
                'arm_id': row['arm_id'],
                'descrip': row['descrip']
            }
    return events


def redcap_unique_event_name(descrip: str, arm_name: str) -> str:
    str_value = descrip + ' ' + arm_name
    return str_value.lower().replace(' ', '_').replace('-', '')


def redcap_event_id_to_unique_event_name(event_id: int) -> str:
    """Map a redcap event_id into its unique name."""
    # This emulates the internal redcap method
    # NOTE: If changes are made to add/remove/rename events in REDcap those must be reflected in new dumps of arms.csv (redcap_events_arms) and metadata.csv (redcap_events_metadata)
    event_id = str(event_id)
    arms = load_arms()
    metadata = load_metadata()
    event_name = redcap_unique_event_name(metadata[event_id]['descrip'],
                                          arms[metadata[event_id]['arm_id']])
    return event_name
