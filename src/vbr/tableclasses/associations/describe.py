"""Represent cases where files describe VBR records.
"""
from ...pgrest import *
from ..constants import Constants

__all__ = ['FileDescribesBiosample', 'FileDescribesSubject']


class FileDescribesMeasurement(AssociationTable):
    """Maps files to the measurements they describe."""

    file_describes_measurement_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey('file.file_id'))
    measurement = Column(Integer, ForeignKey('measurement.measurement_id'))


class FileDescribesBiosample(AssociationTable):
    """Maps files to the biosamples they describe."""

    file_describes_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey('file.file_id'))
    biosample = Column(Integer, ForeignKey('biosample.biosample_id'))


class FileDescribesSubject(AssociationTable):
    """Maps files to associated subjects."""

    file_describes_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file = Column(Integer, ForeignKey('file.file_id'))
    subject = Column(Integer, ForeignKey('subject.subject_id'))
