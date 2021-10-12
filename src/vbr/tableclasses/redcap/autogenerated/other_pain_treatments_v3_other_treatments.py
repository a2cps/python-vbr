"""Autogenerated 2021-10-12T09:26:27.406647 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapOtherPainTreatmentsV3OtherTreatments']

class RcapOtherPainTreatmentsV3OtherTreatments(RcapTable):
    """Other Pain Treatments V3 Other Treatments
    """
    __redcap_form_name = 'other_pain_treatments_v3_other_treatments'
    other_pain_treatments_v3_other_treatments_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    other_pain_treatments_v3_other_treatments_complete = Column(Integer, ForeignKey('status.status_id'))
    # In the PAST 4 WEEKS, how often have you participated in thera...
    # Field Type: radio
    # Choices: 1, Daily or almost daily | 2, 2-4 days/week | 3, Weekly | 4, Less than 1 day/week | 5, Never
    opt_q5_thera_exer = Column(Integer, nullable=False, comments=None)
    # In the PAST 4 WEEKS, how often have you received hands‐on tre...
    # Field Type: radio
    # Choices: 1, Daily or almost daily | 2, 2-4 days/week | 3, Weekly | 4, Less than 1 day/week | 5, Never
    opt_q6_hands_on_trt = Column(Integer, nullable=False, comments=None)
    # In the PAST 4 WEEKS, how often have you applied a treatment f...
    # Field Type: radio
    # Choices: 1, Daily or almost daily | 2, 2-4 days/week | 3, Weekly | 4, Less than 1 day/week | 5, Never
    opt_q7_modality_trt = Column(Integer, nullable=False, comments=None)
    # In the PAST 4 WEEKS, how often have you received behavioral o...
    # Field Type: radio
    # Choices: 1, Daily or almost daily | 2, 2-4 days/week | 3, Weekly | 4, Less than 1 day/week | 5, Never
    opt_q8_mental_hlth_trt = Column(Integer, nullable=False, comments=None)
    # In the PAST 4 WEEKS, how often have you used any anxiety medi...
    # Field Type: radio
    # Choices: 1, Daily or almost daily | 2, 2-4 days/week | 3, Weekly | 4, Less than 1 day/week | 5, Never
    opt_q2_anx_meds = Column(Integer, nullable=False, comments=None)
    # In the PAST 4 WEEKS, how often have you used any prescription...
    # Field Type: radio
    # Choices: 1, Daily or almost daily | 2, 2-4 days/week | 3, Weekly | 4, Less than 1 day/week | 5, Never
    opt_q3_ns_pain_meds = Column(Integer, nullable=False, comments=None)
    # In the PAST 4 WEEKS, how often have you used any THC/CBD or m...
    # Field Type: radio
    # Choices: 1, Daily or almost daily | 2, 2-4 days/week | 3, Weekly | 4, Less than 1 day/week | 5, Never
    opt_q4_cbd = Column(Integer, nullable=False, comments=None)