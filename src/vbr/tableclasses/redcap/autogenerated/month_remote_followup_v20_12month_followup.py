"""Autogenerated 2021-09-02T13:30:49.051536 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapMonthRemoteFollowupV2012MonthFollowup']


class RcapMonthRemoteFollowupV2012MonthFollowup(RcapTable):
    """Month Remote Followup V20 12Month Followup
    """
    __redcap_form_name = 'month_remote_followup_v20_12month_followup'
    month_remote_followup_v20_12month_followup_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    month_remote_followup_v20_12month_followup_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # 1. Please rate your knee pain by choosing the number that bes...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12worstkneepainscl = Column(Integer, nullable=False, comments=None)
    # 2. Please rate your knee pain by choosing the number that bes...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12avgkneepainscl = Column(Integer, nullable=False, comments=None)
    # 3. Please rate how much your knee pain has interfered with yo...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12kneepaininterscl = Column(Integer, nullable=False, comments=None)
    # Please rate the overall QUALITY of your SLEEP in the LAST 7 D...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12sleepqualscl = Column(Integer, nullable=False, comments=None)
    # During the LAST 7 DAYS, how physically active were you?
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12physactscl = Column(Integer, nullable=False, comments=None)
    # During the past 24 hours, did you take any kind of medication...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medkneepainyn = Column(Boolean, nullable=False, comments=None)
    # 6a. If yes, please indicate which medications you took from t...
    # Field Type: descriptive
    # Choices: N/A
    rfu12_dt_1 = Column(String, nullable=False, comments=None)
    # Over-the-counter pain relievers (e.g., acetaminophen Tylenol,...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medkneeotc = Column(Boolean, nullable=False, comments=None)
    # Opioid pain relievers (e.g., oxycodone, Percocet, Nucynta, ta...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medkneeopioid = Column(Boolean, nullable=False, comments=None)
    # THC/CBD or marijuana products (edibles, gummies, CBD oil, wee...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medkneecannabid = Column(Boolean, nullable=False, comments=None)
    # Gabapentin or pregabalin (Neurontin, Lyrica, etc)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medkneegaba = Column(Boolean, nullable=False, comments=None)
    # Duloxetine (Cymbalta) or venlafaxine (Wellbutrin)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medkneedulox = Column(Boolean, nullable=False, comments=None)
    # Other, not specified above
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medkneeother = Column(Boolean, nullable=False, comments=None)
    # Specify other
    # Field Type: text
    # Choices: N/A
    rfu12medkneeothertxt = Column(String, nullable=False, comments=None)
    # 1. Please rate your chest pain by choosing the number that be...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12worstchestpainscl = Column(Integer, nullable=False, comments=None)
    # 2. Please rate your chest pain by choosing the number that be...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12avgchestpainscl = Column(Integer, nullable=False, comments=None)
    # 3. Please rate how much your chest pain has interfered with y...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    rfu12chestpaininterscl = Column(Integer, nullable=False, comments=None)
    # During the past 24 hours, did you take any kind of medication...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medchestpainyn = Column(Boolean, nullable=False, comments=None)
    # Over-the-counter pain relievers (e.g., acetaminophen Tylenol,...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medchestotc = Column(Boolean, nullable=False, comments=None)
    # Opioid pain relievers (e.g., oxycodone, Percocet, Nucynta, ta...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medchestopioid = Column(Boolean, nullable=False, comments=None)
    # THC/CBD or marijuana products (edibles, gummies, CBD oil, wee...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medchestcannabid = Column(Boolean, nullable=False, comments=None)
    # Gabapentin or pregabalin (Neurontin, Lyrica, etc)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medchestgaba = Column(Boolean, nullable=False, comments=None)
    # Duloxetine (Cymbalta) or venlafaxine (Wellbutrin)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medchestdulox = Column(Boolean, nullable=False, comments=None)
    # Other, not specified above
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rfu12medchestother = Column(Boolean, nullable=False, comments=None)
    # Specify other
    # Field Type: text
    # Choices: N/A
    rfu12medchestothertxt = Column(String, nullable=False, comments=None)
