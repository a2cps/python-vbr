"""Autogenerated 2021-11-16T11:37:36.593350 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapAcutePhaseTrajectoryItemsV016MonthDaily"]


class RcapAcutePhaseTrajectoryItemsV016MonthDaily(RcapTable):
    """Acute Phase Trajectory Items V01 6Month Daily"""

    __redcap_form_name = "acute_phase_trajectory_items_v01_6month_daily"
    acute_phase_trajectory_items_v01_6month_daily_id = (
        Constants.SERIAL_PRIMARY_KEY_COLUMN
    )
    acute_phase_trajectory_items_v01_6month_daily_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Date entered
    # Field Type: text
    # Choices: N/A
    traj24wkenterdate = Column(String, nullable=True, comments=None)
    # 1. Please rate your chest pain by choosing the number that be...
    # Field Type: radio
    # Choices: 0, 0 No pain | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Pain as bad as you can imagine
    traj24worstpainscl = Column(Integer, nullable=True, comments=None)
    # 2. Please rate your chest pain by choosing the number that be...
    # Field Type: radio
    # Choices: 0, 0 No pain | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Pain as bad as you can imagine
    traj24avgpainscl = Column(Integer, nullable=True, comments=None)
    # 3. Please rate how much your chest pain has interfered with y...
    # Field Type: radio
    # Choices: 0, 0 Did not interfere | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Completely interfered
    traj24painintfactivscl = Column(Integer, nullable=True, comments=None)
    # Please rate the overall QUALITY of your SLEEP in the past 24 ...
    # Field Type: radio
    # Choices: 0, 0 Extremely poor | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Extremely good
    traj24sleepscl = Column(Integer, nullable=True, comments=None)
    # During the past 24 hours, how physically active were you?
    # Field Type: radio
    # Choices: 0, 0 Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Extremely
    traj24physactscl = Column(Integer, nullable=True, comments=None)
    # During the past 24 hours, did you take any kind of medication...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj24medyn = Column(Boolean, nullable=True, comments=None)
    # 1. Over-the-counter pain relievers (e.g., acetaminophen Tylen...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj24medlist1otc = Column(Boolean, nullable=True, comments=None)
    # 2. Opioid pain relievers (e.g., oxycodone, Percocet, Nucynta,...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj24medlist2opioid = Column(Boolean, nullable=True, comments=None)
    # THC/CBD or marijuana products (edibles, gummies, CBD oil, wee...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj24medlist3thc = Column(Boolean, nullable=True, comments=None)
    # Gabapentin or pregabalin (Neurontin, Lyrica, etc)
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj24medlist4gaba = Column(Boolean, nullable=True, comments=None)
    # Duloxetine (Cymbalta) or venlafaxine (Wellbutrin)
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj24medlist5dulox = Column(Boolean, nullable=True, comments=None)
    # Other, not specified above
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj24medlist6other = Column(Boolean, nullable=True, comments=None)
    # Other, specify
    # Field Type: notes
    # Choices: N/A
    traj24medlist6othertxt = Column(FreeText, nullable=True, comments=None)
