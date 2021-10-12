"""Autogenerated 2021-10-12T09:26:27.404574 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapPatientDemographicsBaselineV03DemographicsI']

class RcapPatientDemographicsBaselineV03DemographicsI(RcapTable):
    """Patient Demographics Baseline V03 Demographics I
    """
    __redcap_form_name = 'patient_demographics_baseline_v03_demographics_i'
    patient_demographics_baseline_v03_demographics_i_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    patient_demographics_baseline_v03_demographics_i_complete = Column(Integer, ForeignKey('status.status_id'))
    # Birth date
    # Field Type: text
    # Choices: N/A
    brthdtc = Column(String, nullable=False, comments=None)
    # Age
    # Field Type: text
    # Choices: N/A
    age = Column(String, nullable=False, comments=None)
    # Sex at birth
    # Field Type: radio
    # Choices: 1, Male | 2, Female | 3, Unknown | 4, Intersex
    sex = Column(Integer, nullable=False, comments=None)
    # Gender identity
    # Field Type: radio
    # Choices: 1, Male | 2, Female | 3, Unknown | 4, Other, specify
    genident = Column(Integer, nullable=False, comments=None)
    # Gender identity - Other, specify
    # Field Type: text
    # Choices: N/A
    genidentoth = Column(String, nullable=False, comments=None)
    # Ethnicity
    # Field Type: radio
    # Choices: 1, Hispanic or Latino, A person of Mexican, Puerto Rican, Cuban, Central or South American or other Spanish culture or origin, regardless of race | 2, Not Hispanic or Latino, A person not of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. An arbitrary ethnic classification | 3, Unknown, Not known, not observed, not recorded, or refused | 4, Not reported, Not provided or available
    ethnic = Column(Integer, nullable=False, comments=None)
    # Race - (Choose all that apply)
    # Field Type: checkbox
    # Choices: 1, American Indian or Alaska Native | 2, Asian | 3, Black or African-American | 4, Native Hawaiian or Pacific Islander | 5, White | 6, Unknown | 7, Not Reported
    dem_race = Column(Integer, nullable=False, comments=None)