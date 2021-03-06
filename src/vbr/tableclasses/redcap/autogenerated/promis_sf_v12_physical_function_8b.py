"""Autogenerated 2021-11-16T11:37:36.451164 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapPromisSfV12PhysicalFunction8B"]


class RcapPromisSfV12PhysicalFunction8B(RcapTable):
    """Promis Sf V12 Physical Function 8B"""

    __redcap_form_name = "promis_sf_v12_physical_function_8b"
    promis_sf_v12_physical_function_8b_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    promis_sf_v12_physical_function_8b_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Are you able to do chores such as vacuuming or yard work?
    # Field Type: radio
    # Choices: 5, Without any difficulty | 4, With a little difficulty | 3, With some difficulty | 2, With much difficulty | 1, Unable to do
    pfadochoresscl = Column(Integer, nullable=True, comments=None)
    # Are you able to go up and down stairs at a normal pace?
    # Field Type: radio
    # Choices: 5, Without any difficulty | 4, With a little difficulty | 3, With some difficulty | 2, With much difficulty | 1, Unable to do
    pfastairsscl = Column(Integer, nullable=True, comments=None)
    # Are you able to go for a walk of at least 15 minutes?
    # Field Type: radio
    # Choices: 5, Without any difficulty | 4, With a little difficulty | 3, With some difficulty | 2, With much difficulty | 1, Unable to do
    pfawalkscl = Column(Integer, nullable=True, comments=None)
    # Are you able to run errands and shop?
    # Field Type: radio
    # Choices: 5, Without any difficulty | 4, With a little difficulty | 3, With some difficulty | 2, With much difficulty | 1, Unable to do
    pfarunerrandsscl = Column(Integer, nullable=True, comments=None)
    # Does your health now limit you in doing two hours of physical...
    # Field Type: radio
    # Choices: 5, Not at all | 4, Very little | 3, Somewhat | 2, Quite a lot | 1, Cannot do
    pfaphyslaborlimitscl = Column(Integer, nullable=True, comments=None)
    # Does your health now limit you in doing moderate work around ...
    # Field Type: radio
    # Choices: 5, Not at all | 4, Very little | 3, Somewhat | 2, Quite a lot | 1, Cannot do
    pfamodwrklimitscl = Column(Integer, nullable=True, comments=None)
    # Does your health now limit you in lifting or carrying groceries?
    # Field Type: radio
    # Choices: 5, Not at all | 4, Very little | 3, Somewhat | 2, Quite a lot | 1, Cannot do
    pfagrocliftlimitscl = Column(Integer, nullable=True, comments=None)
    # Does your health now limit you in doing heavy work around the...
    # Field Type: radio
    # Choices: 5, Not at all | 4, Very little | 3, Somewhat | 2, Quite a lot | 1, Cannot do
    pfaheavyworklimitscl = Column(Integer, nullable=True, comments=None)
