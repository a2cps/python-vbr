"""Autogenerated 2021-11-16T11:37:36.434999 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapOtherMedicalSurgicalTreatmentsIi"]


class RcapOtherMedicalSurgicalTreatmentsIi(RcapTable):
    """Other Medical Surgical Treatments Ii"""

    __redcap_form_name = "other_medical_surgical_treatments_ii"
    other_medical_surgical_treatments_ii_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    other_medical_surgical_treatments_ii_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: text
    # Choices: N/A
    oms1timeframe = Column(String, nullable=True, comments=None)
    # Did you receive any Chemotherapy / Immunotherapy for cancer i...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1chemoyn = Column(Boolean, nullable=True, comments=None)
    # Did you receive any Radiation Therapy for cancer in the past ...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1radtxyn = Column(Boolean, nullable=True, comments=None)
    # In the past [oms1timeframe], have you had any additional sign...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1surgyn = Column(Boolean, nullable=True, comments=None)
    # 3.1 Related to my original knee surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1surgrel = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Knee manipulation
    oms1relmanipultn = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Infection at surgical site
    oms1relinfection = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Revision of knee replacement
    oms1relrevision = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Other
    oms1relother = Column(Boolean, nullable=True, comments=None)
    # Other specify
    # Field Type: text
    # Choices: N/A
    oms1relothertxt = Column(String, nullable=True, comments=None)
    # 3.2 Unrelated to my original knee surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1surgunr = Column(Boolean, nullable=True, comments=None)
    # Choose all that apply
    # Field Type: checkbox
    # Choices: 1, Surgery on the other knee
    oms1unrotherknee = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Surgery on another region
    oms1unrsurgother = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Other
    oms1unrother = Column(Boolean, nullable=True, comments=None)
    # Other specify
    # Field Type: text
    # Choices: N/A
    oms1unrothertxt = Column(String, nullable=True, comments=None)
    # In the past [oms1timeframe], have you had any non-scheduled v...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1visityn = Column(Boolean, nullable=True, comments=None)
    # 4.1. Related to my original knee surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1relvisit = Column(Boolean, nullable=True, comments=None)
    # Choose all that apply
    # Field Type: checkbox
    # Choices: 1, Emergency room / Urgent care clinic visit
    oms1relvisited = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Physician office visit
    oms1relvisitoffice = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Other
    oms1relvisitother = Column(Boolean, nullable=True, comments=None)
    # Other specify
    # Field Type: text
    # Choices: N/A
    oms1relvisitothertxt = Column(String, nullable=True, comments=None)
    # 4.2 Unrelated to my original knee surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms1unrvisit = Column(Boolean, nullable=True, comments=None)
    # Choose all that apply
    # Field Type: checkbox
    # Choices: 1, Emergency room / Urgent care clinic visit
    oms1unrvisited = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Physician office visit
    oms1unrvisitoffice = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Other
    oms1unrvisitother = Column(Boolean, nullable=True, comments=None)
    # Other specify
    # Field Type: text
    # Choices: N/A
    oms1unrvisitothertxt = Column(String, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: text
    # Choices: N/A
    oms2timeframe = Column(String, nullable=True, comments=None)
    # Did you receive any Chemotherapy / Immunotherapy for cancer i...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2chemoyn = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, a. For the cancer associated with your thoracic surgery
    oms2chemosame = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, b. For a different cancer
    oms2chemodiff = Column(Boolean, nullable=True, comments=None)
    # Did you receive any Radiation Therapy for cancer in the past ...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2radtxyn = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, a. For the cancer associated with your thoracic surgery
    oms2radtxsame = Column(Boolean, nullable=True, comments=None)
    # Field Name was empty in Data Dictionary
    # Field Type: checkbox
    # Choices: 1, b. For a different cancer
    oms2radtxdiff = Column(Boolean, nullable=True, comments=None)
    # In the past [oms2timeframe], have you had any additional sign...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2surgyn = Column(Boolean, nullable=True, comments=None)
    # 3.1 Yes, related to my original chest surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2surgrel = Column(Boolean, nullable=True, comments=None)
    # 3.2 Yes, but unrelated to my original chest surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2surgunr = Column(Boolean, nullable=True, comments=None)
    # In the past [oms2timeframe], have you had any non-scheduled v...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2visityn = Column(Boolean, nullable=True, comments=None)
    # 4.1. Yes, related to my original chest surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2relvisit = Column(Boolean, nullable=True, comments=None)
    # Choose all that apply
    # Field Type: checkbox
    # Choices: 1, Emergency room / Urgent care clinic visit
    oms2relvisited = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Physician office visit
    oms2relvisitoffice = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Other
    oms2relvisitother = Column(Boolean, nullable=True, comments=None)
    # Other specify
    # Field Type: text
    # Choices: N/A
    oms2relvisitothertxt = Column(String, nullable=True, comments=None)
    # 4.2 Yes, but unrelated to my original chest surgery
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    oms2unrvisit = Column(Boolean, nullable=True, comments=None)
    # Choose all that apply
    # Field Type: checkbox
    # Choices: 1, Emergency room / Urgent care clinic visit
    oms2unrvisited = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Physician office visit
    oms2unrvisitoffice = Column(Boolean, nullable=True, comments=None)
    #
    # Field Type: checkbox
    # Choices: 1, Other
    oms2unrvisitother = Column(Boolean, nullable=True, comments=None)
    # Other specify
    # Field Type: text
    # Choices: N/A
    oms2unrvisitothertxt = Column(String, nullable=True, comments=None)
