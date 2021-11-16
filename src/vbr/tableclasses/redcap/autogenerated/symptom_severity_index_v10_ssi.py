"""Autogenerated 2021-11-16T11:37:36.443345 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapSymptomSeverityIndexV10Ssi"]


class RcapSymptomSeverityIndexV10Ssi(RcapTable):
    """Symptom Severity Index V10 Ssi"""

    __redcap_form_name = "symptom_severity_index_v10_ssi"
    symptom_severity_index_v10_ssi_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    symptom_severity_index_v10_ssi_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Fatigue
    # Field Type: radio
    # Choices: 0, No problem | 1, Mild | 2, Moderate | 3, Severe
    ssi_fatigue = Column(Integer, nullable=True, comments=None)
    # Trouble thinking or remembering
    # Field Type: radio
    # Choices: 0, No problem | 1, Mild | 2, Moderate | 3, Severe
    ssi_cognitive = Column(Integer, nullable=True, comments=None)
    # Waking up tired (unrefreshed)
    # Field Type: radio
    # Choices: 0, No problem | 1, Mild | 2, Moderate | 3, Severe
    ssi_tired = Column(Integer, nullable=True, comments=None)
    # Have your problems with these symptoms been present for 3 mon...
    # Field Type: yesno
    # Choices: N/A
    ssi_chronicyn = Column(Boolean, nullable=True, comments=None)
    # Pain or cramps in the lower abdomen
    # Field Type: yesno
    # Choices: N/A
    ssi_abdpainyn = Column(Boolean, nullable=True, comments=None)
    # Depression
    # Field Type: yesno
    # Choices: N/A
    ssi_depressyn = Column(Boolean, nullable=True, comments=None)
    # Headache
    # Field Type: yesno
    # Choices: N/A
    ssi_headacheyn = Column(Boolean, nullable=True, comments=None)
