"""Represent data event associations with VBR types.
"""
from ...pgrest import *
from ..constants import Constants

__all__ = [
    'DataEventInContainer', 'DataEventInBiosample', 'DataEventInMeasurement',
    'DataEventInShipment', 'DataEventInSubject', 'DataEventInDataset'
]


class DataEventInBiosample(AssociationTable):
    """Maps data_events to biosamples."""

    data_event_in_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event = Column(Integer, ForeignKey('data_event.data_event_id', event_action='CASCADE'))
    biosample = Column(Integer, ForeignKey('biosample.biosample_id', event_action='CASCADE'))


class DataEventInContainer(AssociationTable):
    """Maps data_events to containers."""

    data_event_in_container_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event = Column(Integer, ForeignKey('data_event.data_event_id', event_action='CASCADE'))
    container = Column(Integer, ForeignKey('container.container_id', event_action='CASCADE'))


class DataEventInMeasurement(AssociationTable):
    """Maps data_events associated with measurements."""
    data_event_in_measurement_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event = Column(Integer, ForeignKey('data_event.data_event_id', event_action='CASCADE'))
    measurement = Column(Integer, ForeignKey('measurement.measurement_id', event_action='CASCADE'))


class DataEventInShipment(AssociationTable):
    """Maps data_events associated with shipments."""
    data_event_in_shipment_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event = Column(Integer, ForeignKey('data_event.data_event_id', event_action='CASCADE'))
    shipment = Column(Integer, ForeignKey('shipment.shipment_id', event_action='CASCADE'))


class DataEventInSubject(AssociationTable):
    """Maps data_events associated with each subject."""

    data_event_in_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event = Column(Integer, ForeignKey('data_event.data_event_id', event_action='CASCADE'))
    subject = Column(Integer, ForeignKey('subject.subject_id', event_action='CASCADE'))


class DataEventInDataset(AssociationTable):
    """Maps data_events to datasets."""

    data_event_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event = Column(Integer, ForeignKey('data_event.data_event_id', event_action='CASCADE'))
    dataset = Column(Integer, ForeignKey('dataset.dataset_id', event_action='CASCADE'))
