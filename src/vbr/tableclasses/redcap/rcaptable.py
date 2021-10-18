from ...pgrest import *
from ..constants import Constants
from .rcconstants import REDCapConstants


class RcapTable(Table):
    """Parent class for REDCap-derived tables
    """
    # tracking_id (subject GUID)
    # tracking_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct.
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # RCap record_id identifying subject
    record_id = REDCapConstants.RECORD_ID
    # TODO - Do we need a uniqueness constraint on the set of id fields?
    data_event_id = Column(Integer,
                           ForeignKey("data_event.data_event_id"),
                           nullable=True)
    biosample_id = Column(Integer,
                          ForeignKey("biosample.biosample_id"),
                          nullable=True)
    measurement_id = Column(Integer,
                            ForeignKey("measurement.measurement_id"),
                            nullable=True)
    subject_id = Column(Integer,
                        ForeignKey("subject.subject_id"),
                        nullable=True)

    @classmethod
    def _links(cls):
        # Update this with any new linkages established by adding FK constraints above
        return ('data_event', 'biosample', 'measurement', 'subject')

    @classmethod
    def link_column_names(cls):
        """Return names of columns linked by foreign key constraints."""
        cols = [c + '_id' for c in cls._links()]
        return tuple(cols)
