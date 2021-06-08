from ..pgrest import *
from .constants import Constants

# https://stackoverflow.com/questions/30406808/flask-sqlalchemy-difference-between-association-model-and-association-table-fo


class BiosampleFromSubject(AssociationTable):
    """Maps biosamples to subjects."""

    biosample_from_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    biosample_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    biosample_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_biosample_id_namespace_biosample_local_id = UniqueConstraint(
        'biosample_id_namespace', 'biosample_local_id')
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))
    subject_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    subject_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_subject_id_namespace_subject_local_id = UniqueConstraint(
        'subject_id_namespace', 'subject_local_id')
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


class BiosampleInDataset(AssociationTable):
    """Maps biosamples to datasets."""

    biosample_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    biosample_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    biosample_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_biosample_id_namespace_biosample_local_id = UniqueConstraint(
        'biosample_id_namespace', 'biosample_local_id')
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))
    dataset_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    dataset_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_dataset_id_namespace_dataset_local_id = UniqueConstraint(
        'dataset_id_namespace', 'dataset_local_id')
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))


class DataEventInBiosample(AssociationTable):
    """Maps data_events to biosamples."""

    data_event_in_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    data_event_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_data_event_id_namespace_data_event_local_id = UniqueConstraint(
        'data_event_id_namespace', 'data_event_local_id')
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    biosample_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    biosample_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_biosample_id_namespace_biosample_local_id = UniqueConstraint(
        'biosample_id_namespace', 'biosample_local_id')
    biosample_id = Column(Integer, ForeignKey=('biosample.biosample_id'))


class DataEventInDataset(AssociationTable):
    """Maps data_events to datasets."""

    data_event_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    data_event_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_data_event_id_namespace_data_event_local_id = UniqueConstraint(
        'data_event_id_namespace', 'data_event_local_id')
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    dataset_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    dataset_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_dataset_id_namespace_dataset_local_id = UniqueConstraint(
        'data_event_id_namespace', 'data_event_local_id')
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))


class DataEventInSubject(AssociationTable):
    """Maps data_events associated with each subject."""

    data_event_in_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    data_event_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    data_event_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_data_event_id_namespace_data_event_local_id = UniqueConstraint(
        'data_event_id_namespace', 'data_event_local_id')
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))
    subject_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    subject_local_id = Constants.STRING_LOCALID_COLUMN
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


class DatasetDefinedByProject(AssociationTable):
    """Maps datasets to their associated projects.""" 

    dataset_defined_by_project_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    dataset_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    dataset_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_dataset_id_namespace_dataset_local_id = UniqueConstraint(
        'data_event_id_namespace', 'data_event_local_id')
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))
    project_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    project_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_project_id_namespace_project_local_id = UniqueConstraint(
        'project_id_namespace', 'project_local_id')
    project_id = Column(Integer, ForeignKey('project.project_id'))


# TODO - CHECK constraint to avoid self-referencing
class DatasetInDataset(AssociationTable):
    """Maps dataset hierarchy and “cross-cut” collections."""

    dataset_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    child_dataset_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    child_dataset_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_child_dataset_id_namespace_child_dataset_local_id = UniqueConstraint(
        'child_dataset_id_namespace', 'child_dataset_local_id')
    child_dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))
    parent_dataset_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    parent_dataset_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_parent_dataset_id_namespace_parent_dataset_local_id = UniqueConstraint(
        'parent_dataset_id_namespace', 'parent_dataset_local_id')
    parent_dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))


class FileDescribesBiosample(AssociationTable):
    """Maps files to the biosamples they describe."""

    file_describes_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    file_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_file_id_namespace_file_local_id = UniqueConstraint(
        'file_id_namespace', 'file_local_id')
    file_id = Column(Integer, ForeignKey('file.file_id'))
    biosample_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    biosample_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_iosample_id_namespace_biosample_local_id = UniqueConstraint(
        'biosample_id_namespace', 'biosample_local_id')
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))


class FileDescribesSubject(AssociationTable):
    """Maps files to associated subjects."""

    file_describes_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    file_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_file_id_namespace_file_local_id = UniqueConstraint(
        'file_id_namespace', 'file_local_id')
    file_id = Column(Integer, ForeignKey('file.file_id'))
    subject_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    subject_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_subject_id_namespace_subject_local_id = UniqueConstraint(
        'subject_id_namespace', 'subject_local_id')
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))


class FileInDataEvent(AssociationTable):
    """Maps files to data events which create or alter them."""

    file_in_data_event_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    file_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_file_id_namespace_file_local_id = UniqueConstraint(
        'file_id_namespace', 'file_local_id')
    file_id = Column(Integer, ForeignKey('file.file_id'))
    data_event_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    data_event_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_ata_event_id_namespace_data_event_local_id = UniqueConstraint(
        'data_event_id_namespace', 'data_event_local_id')
    data_event_id = Column(Integer, ForeignKey('data_event.data_event_id'))


class FileInDataset(AssociationTable):
    """Maps files to dataset collections."""

    file_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    file_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_file_id_namespace_file_local_id = UniqueConstraint(
        'file_id_namespace', 'file_local_id')
    file_id = Column(Integer, ForeignKey('file.file_id'))
    dataset_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    dataset_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_dataset_id_namespace_dataset_local_id = UniqueConstraint(
        'dataset_id_namespace', 'dataset_local_id')
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))


class FileInFile(AssociationTable):
    """Maps files to a tar, zip or container file."""

    file_in_file_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    child_file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    child_file_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_child_file_id_namespace_child_file_local_id = UniqueConstraint(
        'child_file_id_namespace', 'child_file_local_id')
    child_file_id = Column(Integer, ForeignKey('file.file_id'))
    parent_file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    parent_file_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_parent_file_id_namespace_parent_file_local_id = UniqueConstraint(
        'parent_file_id_namespace', 'parent_file_local_id')
    parent_file_id = Column(Integer, ForeignKey('file.file_id'))


class ProtocolInProtocol(AssociationTable):
    """Maps protocol (event_type) hierarchy and 'cross-cut' collections."""

    protocol_in_protocol_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    child_protocol_id = Column(Integer, ForeignKey('protocol.protocol_id'))
    parent_protocol_id = Column(Integer, ForeignKey('protocol.protocol_id'))


class SubjectInDataset(AssociationTable):
    """Maps subjects to dataset collections."""

    subject_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    subject_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    subject_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_subject_id_namespace_ubject_local_id = UniqueConstraint(
        'subject_id_namespace', 'subject_local_id')
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))
    dataset_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    dataset_local_id = Constants.STRING_LOCALID_COLUMN
    uniq_dataset_id_namespace_dataset_local_id = UniqueConstraint(
        'dataset_id_namespace', 'dataset_local_id')
    dataset_id = Column(Integer, ForeignKey('dataset.dataset_id'))
