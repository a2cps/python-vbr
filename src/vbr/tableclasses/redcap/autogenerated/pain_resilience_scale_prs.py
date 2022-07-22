"""Autogenerated 2022-07-22T11:25:37.607662 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ['RcapPainResilienceScalePrs']

class RcapPainResilienceScalePrs(RcapTable):
    """Pain Resilience Scale Prs
    """
    __redcap_form_name = 'pain_resilience_scale_prs'
    pain_resilience_scale_prs_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    pain_resilience_scale_prs_complete = Column(Integer, ForeignKey('status.status_id'))
    # I will get back out there.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsbackoutscl = Column(Integer, nullable=True, comments=None)
    # I still work to accomplish my goals.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsworkgoalsscl = Column(Integer, nullable=True, comments=None)
    # I push through it.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prspushthroughscl = Column(Integer, nullable=True, comments=None)
    # I try to continue working.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prscontworkscl = Column(Integer, nullable=True, comments=None)
    # I like to stay active.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsstayactivescl = Column(Integer, nullable=True, comments=None)
    # I focus on positive attitude.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsfocuspositivescl = Column(Integer, nullable=True, comments=None)
    # I keep a positive attitude.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsposattitudescl = Column(Integer, nullable=True, comments=None)
    # It doesn't affect my happiness.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsnotaffecthappyscl = Column(Integer, nullable=True, comments=None)
    # I still find joy in my life.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsfindjoyscl = Column(Integer, nullable=True, comments=None)
    # I keep a hopeful attitude.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prshopefulscl = Column(Integer, nullable=True, comments=None)
    # I don't let it get me down.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsnotgetdownscl = Column(Integer, nullable=True, comments=None)
    # I don't let it upset me.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsnotupsetscl = Column(Integer, nullable=True, comments=None)
    # I avoid negative thoughts.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsavoidnegativescl = Column(Integer, nullable=True, comments=None)
    # I try to stay relaxed.
    # Field Type: radio
    # Choices: 0, 0 - Not at all | 1, 1 - To a slight degree | 2, 2 - To a moderate degree | 3, 3 - To a great degree | 4, 4 - All the time
    prsstayrelaxscl = Column(Integer, nullable=True, comments=None)