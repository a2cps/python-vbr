from ...pgrest import *
from ..constants import Constants

__all__ = [
    'DataEventInContainer', 'DataEventInBiosample', 'DataEventInMeasurement',
    'DataEventInShipment', 'DataEventInSubject', 'DataEventInDataset'
]


class DataEventInContainer(AssociationTable):
    """Maps data_events to containers."""

    data_event_in_container_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    container_id = Column(Integer, ForeignKey=('container.container_id'))


class DataEventInBiosample(AssociationTable):
    """Maps data_events to biosamples."""

    data_event_in_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    biosample_id = Column(Integer, ForeignKey=('biosample.biosample_id'))


class DataEventInMeasurement(AssociationTable):
    """Maps data_events associated with measurements."""
    data_event_in_measurement_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    measurement_id = Column(Integer, ForeignKey('measurement.measurement_id'))


class DataEventInShipment(AssociationTable):
    """Maps data_events associated with shipments."""
    data_event_in_shipment_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    shipment_id = Column(Integer, ForeignKey('shipment.shipment_id'))


class DataEventInSubject(AssociationTable):
    """Maps data_events associated with each subject."""

    data_event_in_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


class DataEventInDataset(AssociationTable):
    """Maps data_events to datasets."""

    data_event_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))
