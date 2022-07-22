"""Autogenerated 2022-07-22T11:25:37.662457 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ['RcapReportableEventdeviationV03']

class RcapReportableEventdeviationV03(RcapTable):
    """Reportable Eventdeviation V03
    """
    __redcap_form_name = 'reportable_eventdeviation_v03'
    reportable_eventdeviation_v03_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    reportable_eventdeviation_v03_complete = Column(Integer, ForeignKey('status.status_id'))
    # Date of Report Entry (local time)
    # Field Type: text
    # Choices: N/A
    erep_local_dtime = Column(String, nullable=True, comments=None)
    # Submitted by username
    # Field Type: text
    # Choices: N/A
    erep_submit_user = Column(String, nullable=True, comments=None)
    # Date of adverse event
    # Field Type: text
    # Choices: N/A
    erep_ae_date = Column(String, nullable=True, comments=None)
    # Staff/Investigator initials
    # Field Type: text
    # Choices: N/A
    erep_initials = Column(String, nullable=True, comments=None)
    # Visit/encounter involved
    # Field Type: radio
    # Choices: 1, Informed Consent | 2, Baseline (pre-surgery) | 3, 6-weeks post-surgery | 4, 3-months post-surgery | 5, 6-months post surgery | 6, Other or N/A
    erep_visit_inv = Column(Integer, nullable=True, comments=None)
    # A Reportable Event?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    erep_unant_prob = Column(Boolean, nullable=True, comments=None)
    # Is this an adverse event?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    erep_ae_yn = Column(Boolean, nullable=True, comments=None)
    # Date of Adverse event onset
    # Field Type: text
    # Choices: N/A
    erep_onset_date = Column(String, nullable=True, comments=None)
    # Date of Adverse Event resolution
    # Field Type: text
    # Choices: N/A
    erep_resolution_date = Column(String, nullable=True, comments=None)
    # Adverse Event Severity
    # Field Type: radio
    # Choices: 1, Mild (Events require minimal or no treatment and do not interfere with the participant's daily activities) | 2, Moderate (Events result in a low level of inconvenience or concern with the therapeutic measures. Moderate events may cause some interference with functioning.) | 3, Severe (Events interrupt a participant's usual daily activity and may require systemic drug therapy or other treatment. Severe events are usually potentially life-threatening or incapacitating.  Of note, the term "severe" does not necessarily equate to "serious".)
    erep_ae_severity = Column(Integer, nullable=True, comments=None)
    # Relationship to Adverse Event
    # Field Type: radio
    # Choices: 1, Definitely related  (AE is known to occur with the study procedure(s) or there is a temporal relationship between the study procedure(s) and event, that is confirmed by improvement after stopping the procedure (and cannot be explained by participants' clinical or health status). | 2, Possibly/Probably Related  (AE that follows reasonable sequence from administration of study procedure(s),but could readily have been produced by other factors as well.) | 3, Not Related  (There is not a reasonable possibility that the administration of the study procedure(s) caused the event, there is no temporal relationship between the study procedure(s) and event onset, or an alternate etiology has been established.)
    erep_ae_relation = Column(Integer, nullable=True, comments=None)
    # Is the event serious?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    erep_ae_serious = Column(Boolean, nullable=True, comments=None)
    # Description of Adverse Event
    # Field Type: notes
    # Choices: N/A
    erep_ae_desc = Column(FreeText, nullable=True, comments=None)
    # Other Event?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    erep_oe = Column(Boolean, nullable=True, comments=None)
    # Date of event
    # Field Type: text
    # Choices: N/A
    erep_oe_date = Column(String, nullable=True, comments=None)
    # Description of Event
    # Field Type: notes
    # Choices: N/A
    erep_oe_desc = Column(FreeText, nullable=True, comments=None)
    # Action taken regarding continued participation
    # Field Type: notes
    # Choices: N/A
    erep_action_taken = Column(FreeText, nullable=True, comments=None)
    # Outcome
    # Field Type: notes
    # Choices: N/A
    erep_outcome = Column(FreeText, nullable=True, comments=None)
    # Protocol Deviation
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    erep_prot_dev = Column(Boolean, nullable=True, comments=None)
    # Type of deviation
    # Field Type: radio
    # Choices: 1, Informed Consent | 2, Protocol Deviation-blood drawo | 3, Protocol Deviation-functional testing | 4, Protocol Deviation-QST | 5, Protocol Deviation-imaging | 6, Visit timeline (outside protocol range) | 7, Other
    erep_protdev_type = Column(Integer, nullable=True, comments=None)
    # Description of deviation
    # Field Type: notes
    # Choices: N/A
    erep_protdev_desc = Column(FreeText, nullable=True, comments=None)
    # Corrective Action Plan
    # Field Type: notes
    # Choices: N/A
    erep_protdev_caplan = Column(FreeText, nullable=True, comments=None)
    # Is this event related to COVID-19?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    erep_rel_covid19 = Column(Boolean, nullable=True, comments=None)
    # Additional documentation available?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    erep_add_doc_yn = Column(Boolean, nullable=True, comments=None)
    # If yes, where?
    # Field Type: checkbox
    # Choices: 1, Electronic Medical Record | 2, Document uploaded to REDCap
    erep_whereavail = Column(Integer, nullable=True, comments=None)
    # Upload File #1: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_1 = Column(String, nullable=True, comments=None)
    # Upload File #2: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_2 = Column(String, nullable=True, comments=None)
    # Upload File #3: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_3 = Column(String, nullable=True, comments=None)
    # Upload File #4: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_4 = Column(String, nullable=True, comments=None)
    # Upload File #5: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_5 = Column(String, nullable=True, comments=None)
    # Upload File #6: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_6 = Column(String, nullable=True, comments=None)
    # Upload File #7: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_7 = Column(String, nullable=True, comments=None)
    # Upload File #8: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_8 = Column(String, nullable=True, comments=None)
    # Upload File #9: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_9 = Column(String, nullable=True, comments=None)
    # Upload File #10: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_10 = Column(String, nullable=True, comments=None)
    # Upload File #11: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_11 = Column(String, nullable=True, comments=None)
    # Upload File #12: Description
    # Field Type: text
    # Choices: N/A
    erep_file_descript_12 = Column(String, nullable=True, comments=None)
    # Additional information or comments
    # Field Type: notes
    # Choices: N/A
    erep_addinfo = Column(FreeText, nullable=True, comments=None)