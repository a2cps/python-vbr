"""Autogenerated 2021-11-16T11:37:36.541983 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapDailyItems6MoV036MonthDaily"]


class RcapDailyItems6MoV036MonthDaily(RcapTable):
    """Daily Items 6 Mo V03 6Month Daily"""

    __redcap_form_name = "daily_items_6_mo_v03_6month_daily"
    daily_items_6_mo_v03_6month_daily_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    daily_items_6_mo_v03_6month_daily_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # 1. Please rate your knee pain by choosing the number that bes...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    traj6moworstkneepainscl = Column(Integer, nullable=True, comments=None)
    # 2. Please rate your knee pain by choosing the number that bes...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    traj6moavgkneepainscl = Column(Integer, nullable=True, comments=None)
    # 3. Please rate how much your knee pain has interfered with yo...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    traj6mokneepaininterscl = Column(Integer, nullable=True, comments=None)
    # Please rate the overal QUALITY of your SLEEP in the past 24 h...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    traj6mosleepqualscl = Column(Integer, nullable=True, comments=None)
    # During the past 24 hours, how physically active were you?
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    traj6mophysactscl = Column(Integer, nullable=True, comments=None)
    # During the past 24 hours, did you take any kind of medication...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    traj6mopainmeduseyn = Column(Boolean, nullable=True, comments=None)
    # Over-the-counter pain relievers (e.g., acetaminophen Tylenol,...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    traj6mootcuseyn = Column(Boolean, nullable=True, comments=None)
    # Opioid pain relievers (e.g., oxycodone, Percocet, Nucynta, ta...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    traj6moopiateuseyn = Column(Boolean, nullable=True, comments=None)
    # THC/CBD or marijuana products (edibles, gummies, CBD oil, wee...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    traj6mocannabuseyn = Column(Boolean, nullable=True, comments=None)
    # Gabapentin or pregabalin (Neurontin, Lyrica, etc)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    traj6mogabapuseyn = Column(Boolean, nullable=True, comments=None)
    # Duloxetine (Cymbalta) or venlafaxine (Wellbutrin)
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    traj6moduloxuseyn = Column(Boolean, nullable=True, comments=None)
    # Other, not specified above
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    traj6mootheruseyn = Column(Boolean, nullable=True, comments=None)
