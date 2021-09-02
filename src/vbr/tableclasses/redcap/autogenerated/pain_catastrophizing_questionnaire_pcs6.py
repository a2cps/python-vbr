"""Autogenerated 2021-09-02T13:30:48.995184 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapPainCatastrophizingQuestionnairePcs6']


class RcapPainCatastrophizingQuestionnairePcs6(RcapTable):
    """Pain Catastrophizing Questionnaire Pcs6
    """
    __redcap_form_name = 'pain_catastrophizing_questionnaire_pcs6'
    pain_catastrophizing_questionnaire_pcs6_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    pain_catastrophizing_questionnaire_pcs6_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: descriptive
    # Choices: N/A
    pcs_dt_1 = Column(String, nullable=False, comments=None)
    # It's awful and I feel that it overwhelms me
    # Field Type: radio
    # Choices: 0, Not at all | 1, To a slight degree | 2, To a moderate degree | 3, To a great degree | 4, All the time
    pcqpainawfulovrwhlmscl = Column(Integer, nullable=False, comments=None)
    # I feel I can't stand it anymore
    # Field Type: radio
    # Choices: 0, Not at all | 1, To a slight degree | 2, To a moderate degree | 3, To a great degree | 4, All the time
    pcqfeelcantwithstandscl = Column(Integer, nullable=False, comments=None)
    # I become afraid that the pain will get worse
    # Field Type: radio
    # Choices: 0, Not at all | 1, To a slight degree | 2, To a moderate degree | 3, To a great degree | 4, All the time
    pcqafraidpainworsescl = Column(Integer, nullable=False, comments=None)
    # I keep thinking about how much it hurts
    # Field Type: radio
    # Choices: 0, Not at all | 1, To a slight degree | 2, To a moderate degree | 3, To a great degree | 4, All the time
    pcqhurtscl = Column(Integer, nullable=False, comments=None)
    # I keep thinking about how badly I want the pain to stop
    # Field Type: radio
    # Choices: 0, Not at all | 1, To a slight degree | 2, To a moderate degree | 3, To a great degree | 4, All the time
    pcqpainstopscl = Column(Integer, nullable=False, comments=None)
    # I wonder whether something serious may happen
    # Field Type: radio
    # Choices: 0, Not at all | 1, To a slight degree | 2, To a moderate degree | 3, To a great degree | 4, All the time
    pcqseriousscl = Column(Integer, nullable=False, comments=None)
