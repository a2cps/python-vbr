"""Autogenerated 2021-11-16T11:37:36.527859 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapPatientDemographicsFullPart2V03Demographics"]


class RcapPatientDemographicsFullPart2V03Demographics(RcapTable):
    """Patient Demographics Full Part 2 V03 Demographics"""

    __redcap_form_name = "patient_demographics_full_part_2_v03_demographics"
    patient_demographics_full_part_2_v03_demographics_id = (
        Constants.SERIAL_PRIMARY_KEY_COLUMN
    )
    patient_demographics_full_part_2_v03_demographics_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # What is the highest level of education you have completed?
    # Field Type: radio
    # Choices: 1, Did not complete Secondary School or less than High School | 2, Some Secondary School or High School education | 3, High School or Secondary School degree complete | 4, Associate's or Technical Degree complete | 5, College or Baccalaureate degree complete | 6, Doctoral or Postgraduate education
    edulevel = Column(Integer, nullable=True, comments=None)
    # What is your current employment status?
    # Field Type: radio
    # Choices: 1, Full-time employment, Employment involving the standard or customary working time | 2, Not employed, The state of not having a job | 3, Part-time employment, Employment involving less than the standard or customary working time
    empstat = Column(Integer, nullable=True, comments=None)
    # What category best describes your current relationship status?
    # Field Type: radio
    # Choices: 1, Divorced, Marriage contract has been declared dissolved and inactive | 2, Married, A current marriage contract is active | 3, Never Married, No marriage contract has ever been entered | 4, Separated, A person who is separated from their spouse, whether or not there is a legal arrangement | 5, Widowed, The spouse has died | 6, Domestic Partner, Person declares that a domestic partnership relationship exists
    maristat = Column(Integer, nullable=True, comments=None)
    # What is your annual household income from all sources?
    # Field Type: radio
    # Choices: 1, Less than $10,000 | 2, $10,000-$24,999 | 3, $25,000-$34,999 | 4, $35,000-$49,999 | 5, $50,000-$74,999 | 6, $75,000-$99,999 | 7, $100,000-$149,999 | 8, $150,000-$199,999 | 9, $200,000 or more | 10, Prefer not to answer
    incmlvl = Column(Integer, nullable=True, comments=None)
    # Have you ever applied for, or received, disability insurance ...
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    disabinsind = Column(Boolean, nullable=True, comments=None)
    # How long have you had the type of pain for which you are enro...
    # Field Type: text
    # Choices: N/A
    paindur = Column(String, nullable=True, comments=None)
    # Consider which hand you prefer to use when performing a numbe...
    # Field Type: radio
    # Choices: 1, Do you always or mostly prefer to use the right hand for most activities? | 2, Do you always or mostly prefer to use the left hand for most activities? | 3, Do you prefer to use the right hand for roughly half and the left hand for roughly have of activities?
    dom_hand = Column(Integer, nullable=True, comments=None)
    # Was your surgery delayed due to COVID-19?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    surg_delayed = Column(Boolean, nullable=True, comments=None)
    # Were you or anyone living in your household previously diagno...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    prev_covid19_dx = Column(Boolean, nullable=True, comments=None)
    # 15a. If yes, indicate who (check all that apply)
    # Field Type: checkbox
    # Choices: 1, myself | 2, a family member
    who_dx_in_hh = Column(Integer, nullable=True, comments=None)
    # How tall are you? (in ft and inches)
    # Field Type: text
    # Choices: N/A
    height_ft_part = Column(String, nullable=True, comments=None)
    #
    # Field Type: text
    # Choices: N/A
    height_inches_part = Column(String, nullable=True, comments=None)
    # How much do you weigh (in lbs)?
    # Field Type: text
    # Choices: N/A
    weight_lbs = Column(String, nullable=True, comments=None)
