"""Autogenerated 2021-11-05T15:48:31.968031 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcaptable import RcapTable
from ..rcconstants import REDCapConstants

__all__ = ["RcapStudyVisitFeedbackV03"]


class RcapStudyVisitFeedbackV03(RcapTable):
    """Study Visit Feedback V03"""

    __redcap_form_name = "study_visit_feedback_v03"
    study_visit_feedback_v03_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    study_visit_feedback_v03_complete = Column(Integer, ForeignKey("status.status_id"))
    # Do you have any feedback about today's visit, good or bad, th...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    svf_anyfeedback = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Surveys
    svf_surveys = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 3, Confusing / Not enough explanation | 4, Difficulties with electronic interface | 10, Other
    svf_surveys_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_surveys_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, 6m walk /sit-to-stand tests
    svf_walksts = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 2, Too painful | 3, Confusing / Not enough explanation | 10, Other
    svf_walksts_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_walksts_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, PPTs /Neuropen tests
    svf_ppts = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 3, Confusing / Not enough explanation | 10, Other
    svf_ppts_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_ppts_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Cold water bath test
    svf_coldwb = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 2, Too painful | 3, Confusing / Not enough explanation | 10, Other
    svf_coldwb_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_coldwb_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Blood draw
    svf_bdraw = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Took too long | 2, Too painful | 5, Difficulty getting access | 10, Other
    svf_bdraw_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_bdraw_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Cuff pressure test (pre- or during imaging)
    svf_cuffp = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 2, Too painful | 3, Confusing / Not enough explanation | 10, Other
    svf_cuffp_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_cuffp_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, MRI test (other than cuff portion)
    svf_mri = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 6, Claustrophobia concerns | 3, Not enough explanation | 10, Other
    svf_mri_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_mri_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, General / Other not included above
    svf_general = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 7, Logistics (finding where to go, parking) | 8, Visit too long overall | 9, Reimbursement concerns | 10, Other
    svf_general_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_general_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Coughing and deep breathing test
    svf_cgh_dbr = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 3, Confusing / Not enough explanation | 10, Other
    svf_cgh_dbr_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_cgh_dbr_other = Column(String, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, Allodynia test
    svf_allodynia = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: radio
    # Choices: 1, Too long | 3, Confusing / Not enough explanation | 10, Other
    svf_allodynia_fb = Column(Integer, nullable=True, comments=None)
    # Other, specify
    # Field Type: text
    # Choices: N/A
    svf_allodynia_other = Column(String, nullable=True, comments=None)
