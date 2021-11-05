"""Autogenerated 2021-11-05T15:48:31.852202 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcaptable import RcapTable
from ..rcconstants import REDCapConstants

__all__ = ["RcapPainsleepDurationSleepIi"]


class RcapPainsleepDurationSleepIi(RcapTable):
    """Painsleep Duration Sleep Ii"""

    __redcap_form_name = "painsleep_duration_sleep_ii"
    painsleep_duration_sleep_ii_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    painsleep_duration_sleep_ii_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: text
    # Choices: N/A
    sleepnighthourmindurhrs = Column(String, nullable=True, comments=None)
    # and
    # Field Type: text
    # Choices: N/A
    sleepnighthourmindurmins = Column(String, nullable=True, comments=None)
