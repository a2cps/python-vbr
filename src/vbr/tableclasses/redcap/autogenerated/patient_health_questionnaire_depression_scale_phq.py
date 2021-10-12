"""Autogenerated 2021-10-12T09:26:27.433330 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapPatientHealthQuestionnaireDepressionScalePhq']

class RcapPatientHealthQuestionnaireDepressionScalePhq(RcapTable):
    """Patient Health Questionnaire Depression Scale Phq
    """
    __redcap_form_name = 'patient_health_questionnaire_depression_scale_phq'
    patient_health_questionnaire_depression_scale_phq_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    patient_health_questionnaire_depression_scale_phq_complete = Column(Integer, ForeignKey('status.status_id'))
    # Little interest or pleasure in doing things
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqlitintrstscore = Column(Integer, nullable=False, comments=None)
    # Feeling down, depressed, or hopeless
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqdeprssnscore = Column(Integer, nullable=False, comments=None)
    # Trouble falling or staying asleep, or sleeping too much
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqsleepimpairscore = Column(Integer, nullable=False, comments=None)
    # Feeling tired or having little energy
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqtirdlittleenrgyscore = Column(Integer, nullable=False, comments=None)
    # Poor appetite or overeating
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqabnrmldietscore = Column(Integer, nullable=False, comments=None)
    # Feeling bad about yourself, or that you are a failure, or hav...
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqflngfailrscore = Column(Integer, nullable=False, comments=None)
    # Trouble concentrating on things, such as reading the newspape...
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqconcntrtnimprmntscore = Column(Integer, nullable=False, comments=None)
    # Moving or speaking so slowly that other people could have not...
    # Field Type: radio
    # Choices: 0, Not<br>at all<br>0 | 1, Several<br>days<br>1 | 2, More than<br>half<br>the days<br>2 | 3, Nearly<br>every day<br>3
    phqmovmntspchimprmntscore = Column(Integer, nullable=False, comments=None)