"""Represent cases where files describe VBR records.
"""
from ...pgrest import *
from ..constants import Constants

__all__ = ['FileDescribesBiosample', 'FileDescribesSubject']


class FileDescribesMeasurement(AssociationTable):
    """Maps files to the measurements they describe."""

    file_describes_measurement_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey('file.file_id', event_action='CASCADE'))
    measurement = Column(Integer, ForeignKey('measurement.measurement_id', event_action='CASCADE'))


class FileDescribesBiosample(AssociationTable):
    """Maps files to the biosamples they describe."""

    file_describes_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey('file.file_id', event_action='CASCADE'))
    biosample = Column(Integer, ForeignKey('biosample.biosample_id', event_action='CASCADE'))


class FileDescribesSubject(AssociationTable):
    """Maps files to associated subjects."""

    file_describes_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey('file.file_id', event_action='CASCADE'))
    subject = Column(Integer, ForeignKey('subject.subject_id', event_action='CASCADE'))
