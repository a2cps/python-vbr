from vbr.pgrest import *
from .constants import Constants

__all__ = ['VbrRedcapEvent']

class VbrSysEvent(Table):
    """Base class for VBR-specific logging events.
    """
    identifier = Column(LocalId, unique=True, comments="Externally-resolvable identifier")
    created = Column(CreatedTimeStamp,
                     nullable=True,
                     comments='When created')
    updated = Column(UpdatedTimeStamp,
                     nullable=True,
                     comments='When created')
    status = Column(String, comments="Event status")

class VbrRedcapEvent(VbrSysEvent):
    """Events sourced from REDcap -> VBR integration
    """
    internal_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    project_id = Column(Integer)
    record = Column(String)
    instrument = Column(String)
    instrument_complete = Column(Integer)
    event_id = Column(Integer)
