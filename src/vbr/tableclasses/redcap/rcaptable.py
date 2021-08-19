from ...pgrest import *
from ..constants import Constants
from .rcconstants import REDCapConstants


class RcapTable(Table):
    """Subclass for REDCap-derived tables
    """
    #persistent_id (subject GUID)
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct.
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # RCap record_id identifying subject
    record_id = REDCapConstants.RECORD_ID
