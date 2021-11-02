"""Represent nested relations of the same type.
"""
from ...pgrest import *
from ..constants import Constants

__all__ = ['DatasetInDataset', 'FileInFile']

# class ContainerInContainer(AssociationTable):
#     """Maps containers inside other containers."""
#     container_in_container_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
#     # Constrained to be unique so that a container can only be directly inside ONE other
#     container = Column(Integer,
#                        ForeignKey('container.container_id'),
#                        unique=True)
#     parent_container = Column(Integer, ForeignKey('container.container_id'))


class DatasetInDataset(AssociationTable):
    """Maps dataset hierarchy and “cross-cut” collections."""

    dataset_in_dataset_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    dataset = Column(Integer, ForeignKey('dataset.dataset_id', event_action='CASCADE'))
    parent_dataset = Column(Integer, ForeignKey('dataset.dataset_id', event_action='CASCADE'))


class FileInFile(AssociationTable):
    """Maps files to a tar, zip or container file."""

    file_in_file_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # child_file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    # child_file_local_id = Constants.STRING_LOCALID_COLUMN
    # uniq_child_file_id_namespace_child_file_local_id = UniqueConstraint(
    #     'child_file_id_namespace', 'child_file_local_id')
    file = Column(Integer, ForeignKey('file.file_id', event_action='CASCADE'))
    # parent_file_id_namespace = Constants.STRING_NAMESPACE_COLUMN
    # parent_file_local_id = Constants.STRING_LOCALID_COLUMN
    # uniq_parent_file_id_namespace_parent_file_local_id = UniqueConstraint(
    #     'parent_file_id_namespace', 'parent_file_local_id')
    parent_file = Column(Integer, ForeignKey('file.file_id', event_action='CASCADE'))


class ProtocolInProtocol(AssociationTable):
    """Maps protocol (event_type) hierarchy and 'cross-cut' collections."""

    protocol_in_protocol_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    protocol = Column(Integer, ForeignKey('protocol.protocol_id', event_action='CASCADE'))
    parent_protocol = Column(Integer, ForeignKey('protocol.protocol_id', event_action='CASCADE'))
