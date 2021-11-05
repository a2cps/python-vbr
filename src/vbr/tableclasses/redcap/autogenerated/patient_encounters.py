"""Autogenerated 2021-11-05T15:48:31.970884 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcaptable import RcapTable
from ..rcconstants import REDCapConstants

__all__ = ["RcapPatientEncounters"]


class RcapPatientEncounters(RcapTable):
    """Patient Encounters"""

    __redcap_form_name = "patient_encounters"
    patient_encounters_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    patient_encounters_complete = Column(Integer, ForeignKey("status.status_id"))
    # Enter date and time of this patient encounter
    # Field Type: text
    # Choices: N/A
    pe_datetime = Column(String, nullable=True, comments=None)
    # Staff member initials
    # Field Type: text
    # Choices: N/A
    pe_staff_init = Column(String, nullable=True, comments=None)
