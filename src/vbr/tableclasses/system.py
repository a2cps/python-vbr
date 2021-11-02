from vbr.pgrest import *
from .constants import Constants

__all__ = ['VbrSysEventTable', 'VbrRedcapEvent']

STATUSES = ['CREATED', 'PROCESSING', 'COMPLETE', 'FAILED']


class SysEventStatus(String):
    """Custom string type for System Events.
    """
    @classmethod
    def autopopulate(cls, value):
        if value is not None:
            value = value.upper()
            return cls.validated(value)
        else:
            return STATUSES[0]

    @classmethod
    def validated(cls, value):
        """Returns value if valid, raises ValueError if not
        """
        if value in STATUSES:
            return value
        else:
            raise ValueError('Unknown system event status {0}'.format(value))

    @classmethod
    def instantiate(cls, value):
        return cls.autopopulate(value)

    @classmethod
    def cast(cls, value):
        if value is None:
            return cls.autopopulate(value)
        else:
            return str(value).upper()


class VbrSysEventTable(Table):
    """Base class for VBR-specific logging events.
    """
    local_id = Column(LocalId, unique=True, comments="Public identifier")
    created = Column(CreatedTimeStamp, nullable=True, comments='When created')
    updated = Column(UpdatedTimeStamp, nullable=True, comments='When created')
    event_status = Column(SysEventStatus,
                          default=STATUSES[0],
                          comments="Event status")

    def set_status(self, status: str) -> str:
        """Set event status with validation.
        """
        setattr(self, 'event_status',
                SysEventStatus.validated(SysEventStatus.cast(status)))

    def get_status(self) -> str:
        """Get event status.
        """
        return getattr(self, 'event_status')


class VbrRedcapEvent(VbrSysEventTable):
    """Event sourced from REDcap -> VBR integrations.
    """
    internal_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    project_id = Column(Integer, nullable=True)
    record = Column(String, nullable=True)
    instrument = Column(String, nullable=True)
    instrument_complete = Column(Integer, nullable=True)
    event_id = Column(Integer, nullable=True)
