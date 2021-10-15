from ...pgrest import *
from ..constants import Constants

__all__ = [
    'BiosampleInSubject', 'BiosampleInDataset', 'ContainerInShipment',
    'DatasetInProject', 'FileInDataEvent', 'FileInDataset',
    'MeasurementInBiosample', 'SubjectInDataset'
]


class BiosampleInSubject(AssociationTable):
    """Maps biosamples to subjects."""

    biosample_from_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


class BiosampleInDataset(AssociationTable):
    """Maps biosamples to datasets."""

    biosample_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))


class ContainerInShipment(AssociationTable):
    """Maps containers inside other shipments."""
    container_in_shipment_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # Constrained to be unique so that a container can only be directly inside ONE other shipment
    container_id = Column(Integer,
                          ForeignKey('container.container_id'),
                          unique=True)
    shipment_id = Column(Integer, ForeignKey('shipment.shipment_id'))


class DatasetInProject(AssociationTable):
    """Maps datasets to their associated projects."""

    dataset_defined_by_project_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))
    project_id = Column(Integer, ForeignKey('project.project_id'))


class FileInDataEvent(AssociationTable):
    """Maps files to data events which create or alter them."""

    file_in_data_event_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id = Column(Integer, ForeignKey('file.file_id'))
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))


class FileInDataset(AssociationTable):
    """Maps files to dataset collections."""
    file_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id = Column(Integer, ForeignKey('file.file_id'))
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))


class MeasurementInBiosample(AssociationTable):
    """Maps measurements to biosamples."""
    measurement_in_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    measurement_id = Column(Integer, ForeignKey('measurement.measurement_id'))
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))


class SubjectInDataset(AssociationTable):
    """Maps subjects to dataset collections."""
    subject_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))