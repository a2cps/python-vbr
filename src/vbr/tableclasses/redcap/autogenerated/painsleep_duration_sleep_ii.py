"""Autogenerated 2022-07-22T11:25:37.598972 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ['RcapPainsleepDurationSleepIi']

class RcapPainsleepDurationSleepIi(RcapTable):
    """Painsleep Duration Sleep Ii
    """
    __redcap_form_name = 'painsleep_duration_sleep_ii'
    painsleep_duration_sleep_ii_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    painsleep_duration_sleep_ii_complete = Column(Integer, ForeignKey('status.status_id'))
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: text
    # Choices: N/A
    sleepnighthourmindurhrs = Column(String, nullable=True, comments=None)
    # and
    # Field Type: text
    # Choices: N/A
    sleepnighthourmindurmins = Column(String, nullable=True, comments=None)