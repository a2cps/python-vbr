"""Autogenerated 2021-10-12T09:26:27.500151 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapSelfadministeredComorbidityQuestionnaireV4Scq']

class RcapSelfadministeredComorbidityQuestionnaireV4Scq(RcapTable):
    """Selfadministered Comorbidity Questionnaire V4 Scq
    """
    __redcap_form_name = 'selfadministered_comorbidity_questionnaire_v4_scq'
    selfadministered_comorbidity_questionnaire_v4_scq_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    selfadministered_comorbidity_questionnaire_v4_scq_complete = Column(Integer, ForeignKey('status.status_id'))
    # Do you have heart disease?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqheartdx = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqheartdxtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have high blood pressure?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqhtndx = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqhtntreat = Column(Boolean, nullable=False, comments=None)
    # Do you have high cholesterol and/or triglyceride levels?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqhchol = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqhcholtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have lung disease?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqlungdx = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqlungdxtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have diabetes?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqdm = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqdmtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have cerebrovascular disease?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqcerebrovdx = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqcerebrovdxtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have kidney disease?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqkidneydx = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqkidneydxtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have liver disease?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqliverdx = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqliverdxtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have anemia or other blood disease?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqblooddx = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqblooddxtreat = Column(Boolean, nullable=False, comments=None)
    # Do you or have you had cancer?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqcancer = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqcancertreat = Column(Boolean, nullable=False, comments=None)
    # Do you have depression?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqdepressn = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqdepressntreat = Column(Boolean, nullable=False, comments=None)
    # Do you have an anxiety disorder?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqanxdis = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqanxdistreat = Column(Boolean, nullable=False, comments=None)
    # Do you have a neurological disorder?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqneurodis = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqneurodistreat = Column(Boolean, nullable=False, comments=None)
    # Do you have a thyroid disorder?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqthyroid = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqthyroidtreat = Column(Boolean, nullable=False, comments=None)
    # Do you have a gastrointestinal disorder?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqgastro = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqgastrotreat = Column(Boolean, nullable=False, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqra = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqratreat = Column(Boolean, nullable=False, comments=None)
    # Other than osteoarthritis, do you have a chronic pain condition?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqcpcond = Column(Boolean, nullable=False, comments=None)
    # If yes, which of the following pain conditions(check all that...
    # Field Type: checkbox
    # Choices: 1, Fibromyalgia or widespread pain | 2, Migraines or severe headaches | 3, Back or neck pain | 4, Temporomandibular disorder | 5, Other isolated joint-specific pains (e.g., tendinitis) | 6, Irritable bowel syndrome
    scqpconds = Column(Integer, nullable=False, comments=None)
    # Do you receive treatment for any you checked?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqpcondstreat = Column(Boolean, nullable=False, comments=None)
    # Do you have neuropathy (loss of sensation) or altered sensati...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqneuropathy = Column(Boolean, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqneuropathytreat = Column(Boolean, nullable=False, comments=None)
    # Do you have any other medical problems?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqother1 = Column(Boolean, nullable=False, comments=None)
    # Problem
    # Field Type: text
    # Choices: N/A
    scqother1name = Column(String, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqother1treat = Column(Boolean, nullable=False, comments=None)
    # Do you have any other medical problems?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqother2 = Column(Boolean, nullable=False, comments=None)
    # Problem
    # Field Type: text
    # Choices: N/A
    scqother2name = Column(String, nullable=False, comments=None)
    # Do you receive treatment for it?
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    scqother2treat = Column(Boolean, nullable=False, comments=None)