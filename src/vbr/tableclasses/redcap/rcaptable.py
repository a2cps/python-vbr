from ...pgrest import *
from ..constants import Constants
from .rcconstants import REDCapConstants


class RcapSubjectAssociation(object):
    """Associate a REDcap table entry to a VBR.subject"""
    subject_id = Column(Integer,
                        ForeignKey("subject.subject_id"),
                        nullable=True)


class RcapBiosampleAssociation(object):
    """Associate a REDcap table entry to a VBR.biosample"""
    sample_id = Column(Integer,
                       ForeignKey("biosample.biosample_id"),
                       nullable=True)


class RcapDataEventAssociation(object):
    """Associate a REDcap table entry to a VBR.data_event"""
    data_event_id = Column(Integer,
                           ForeignKey("data_event.data_event_id"),
                           nullable=True)


class RcapTable(RcapSubjectAssociation, RcapBiosampleAssociation,
                RcapDataEventAssociation, Table):
    """Parent class for REDCap-derived tables
    """
    # persistent_id (subject GUID)
    # persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct.
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # RCap record_id identifying subject
    record_id = REDCapConstants.RECORD_ID
    # TODO - Do we need a uniqueness constraint on the set of id fields?
