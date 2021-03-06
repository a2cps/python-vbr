from ...pgrest import *
from ..constants import Constants
from .rcconstants import REDCapConstants
from ..vbr_table import TableVBR


class RcapTable(TableVBR):
    """Parent class for REDCap-derived tables"""

    # tracking_id (subject GUID)
    # tracking_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct.
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)

    # Store record, protocol (which maps to redcap event), and status
    # (which maps to redcap status)
    # RCap record_id identifying subject
    record_id = REDCapConstants.RECORD_ID
    # Mandatory
    protocol_id = Column(
        Integer, ForeignKey("protocol.protocol_id"), comments="VBR protocol"
    )
    # Mandatory
    status_id = Column(Integer, ForeignKey("status.status_id"), comments="VBR status")

    # Optionally, join to biosample, measurement, or subject
    biosample_id = Column(
        Integer,
        ForeignKey("biosample.biosample_id", event_action="CASCADE"),
        nullable=True,
    )
    measurement_id = Column(
        Integer,
        ForeignKey("measurement.measurement_id", event_action="CASCADE"),
        nullable=True,
    )
    subject_id = Column(
        Integer, ForeignKey("subject.subject_id", event_action="CASCADE"), nullable=True
    )

    @classmethod
    def _links(cls):
        # Update this with any new linkages established by adding FK constraints above
        return ("protocol", "status", "biosample", "measurement", "subject")

    @classmethod
    def link_column_names(cls):
        """Return names of columns linked by foreign key constraints."""
        cols = [c + "_id" for c in cls._links()]
        return tuple(cols)
