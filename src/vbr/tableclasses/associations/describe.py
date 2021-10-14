from ...pgrest import *
from ..constants import Constants

__all__ = ['FileDescribesBiosample', 'FileDescribesSubject']


class FileDescribesBiosample(AssociationTable):
    """Maps files to the biosamples they describe."""

    file_describes_biosample_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id = Column(Integer, ForeignKey('file.file_id'))
    biosample_id = Column(Integer, ForeignKey('biosample.biosample_id'))


class FileDescribesSubject(AssociationTable):
    """Maps files to associated subjects."""

    file_describes_subject_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    file_id = Column(Integer, ForeignKey('file.file_id'))
    subject_id = Column(Integer, ForeignKey('subject.subject_id'))
