from vbr.pgrest import *

from .constants import Constants
from .vbr_table import TableVBR

__all__ = ["VbrSysEventTable", "SysEvent"]


class VbrSysEventTable(TableVBR):
    """Base class for VBR-specific logging events."""

    created = Column(CreatedTimeStamp, nullable=True, comments="Created")
    updated = Column(UpdatedTimeStamp, nullable=True, comments="Last updated")
    # 70 == sysevent.created
    status = Column(Integer, ForeignKey("status.status_id"), nullable=True, default=70)


class SysEvent(VbrSysEventTable):
    """Event sourced from REDcap -> VBR integrations."""

    sys_event_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    project_id = Column(Integer, nullable=True)
    record = Column(String, nullable=True)
    instrument = Column(String, nullable=True)
    instrument_complete = Column(Integer, nullable=True)
    event_id = Column(Integer, nullable=True)
