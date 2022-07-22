"""Autogenerated 2022-07-22T11:25:37.615062 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ['RcapTaps1']

class RcapTaps1(RcapTable):
    """Taps1
    """
    __redcap_form_name = 'taps1'
    taps1_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    taps1_complete = Column(Integer, ForeignKey('status.status_id'))
    # In the PAST 12 MONTHS, how often have you used any tobacco pr...
    # Field Type: radio
    # Choices: 0, Daily or Almost Daily | 1, Weekly | 2, Monthly | 3, Less Than Monthly | 4, Never
    tapstobaccoproductscl = Column(Integer, nullable=True, comments=None)
    # How many years have you smoked?
    # Field Type: text
    # Choices: N/A
    tapstobaccoproductscl_yrs = Column(String, nullable=True, comments=None)
    # In the PAST 12 MONTHS, how often have you had 5 or more drink...
    # Field Type: radio
    # Choices: 0, Daily or Almost Daily | 1, Weekly | 2, Monthly | 3, Less Than Monthly | 4, Never
    tapsalcoholusemalescl = Column(Integer, nullable=True, comments=None)
    # In the PAST 12 MONTHS, how often have you had 4 or more drink...
    # Field Type: radio
    # Choices: 0, Daily or Almost Daily | 1, Weekly | 2, Monthly | 3, Less Than Monthly | 4, Never
    tapsalcoholusefemalescl = Column(Integer, nullable=True, comments=None)
    # In the PAST 12 MONTHS, how often have you used any drugs incl...
    # Field Type: radio
    # Choices: 0, Daily or Almost Daily | 1, Weekly | 2, Monthly | 3, Less Than Monthly | 4, Never
    tapsdrugusescl = Column(Integer, nullable=True, comments=None)
    # In the PAST 12 MONTHS, how often have you used any prescripti...
    # Field Type: radio
    # Choices: 0, Daily or Almost Daily | 1, Weekly | 2, Monthly | 3, Less Than Monthly | 4, Never
    tapsprescriptionmedusescl = Column(Integer, nullable=True, comments=None)