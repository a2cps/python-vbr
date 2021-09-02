"""Autogenerated 2021-09-02T13:30:48.979970 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapKneeInjuryOsteoarthritisOutcomeScoreKoos12']


class RcapKneeInjuryOsteoarthritisOutcomeScoreKoos12(RcapTable):
    """Knee Injury Osteoarthritis Outcome Score Koos12
    """
    __redcap_form_name = 'knee_injury_osteoarthritis_outcome_score_koos12'
    knee_injury_osteoarthritis_outcome_score_koos12_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    knee_injury_osteoarthritis_outcome_score_koos12_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # INSTRUCTIONS: This survey asks for your views about your knee...
    # Field Type: descriptive
    # Choices: N/A
    koos_desc = Column(String, nullable=False, comments=None)
    # How often do you experience knee pain?
    # Field Type: radio
    # Choices: 0, Never | 1, Monthly | 2, Weekly | 3, Daily | 4, Always
    koospainfreqscl = Column(Integer, nullable=False, comments=None)
    # Walking on flat surface
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koospainwalkflatscl = Column(Integer, nullable=False, comments=None)
    # Going up or down stairs
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koospainstairsscl = Column(Integer, nullable=False, comments=None)
    # Sitting or lying
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koospainsitlyingscl = Column(Integer, nullable=False, comments=None)
    # Rising from bed
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koosfuncdiffrisesitscl = Column(Integer, nullable=False, comments=None)
    # Standing
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koosfuncdiffstandscl = Column(Integer, nullable=False, comments=None)
    # Getting in/out of a car
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koosfuncdiffcarscl = Column(Integer, nullable=False, comments=None)
    # Twisting/pivoting on your injured knee
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koosfunctwistpivotscl = Column(Integer, nullable=False, comments=None)
    # How often are you aware of your knee problem?
    # Field Type: radio
    # Choices: 0, Never | 1, Monthly | 2, Weekly | 3, Daily | 4, Constantly
    koosqolkneeawarescl = Column(Integer, nullable=False, comments=None)
    # Have you modified your life style to avoid potentially damagi...
    # Field Type: radio
    # Choices: 0, Not at all | 1, Mildly | 2, Moderately | 3, Severely | 4, Extremely
    koosqollifestylemodscl = Column(Integer, nullable=False, comments=None)
    # How much are you troubled with lack of confidence in your knee?
    # Field Type: radio
    # Choices: 0, Not at all | 1, Mildly | 2, Moderately | 3, Severely | 4, Extremely
    koosqolconfidencescl = Column(Integer, nullable=False, comments=None)
    # In general, how much difficulty do you have with your knee?
    # Field Type: radio
    # Choices: 0, None | 1, Mild | 2, Moderate | 3, Severe | 4, Extreme
    koosqolkneedifficultyscl = Column(Integer, nullable=False, comments=None)
