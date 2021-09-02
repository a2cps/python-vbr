"""Autogenerated 2021-09-02T15:55:09.551352 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapAcutePhaseTrajectoryItemsV05AcuteDaily']

class RcapAcutePhaseTrajectoryItemsV05AcuteDaily(RcapTable):
    """Acute Phase Trajectory Items V05 Acute Daily
    """
    __redcap_form_name = 'acute_phase_trajectory_items_v05_acute_daily'
    acute_phase_trajectory_items_v05_acute_daily_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    acute_phase_trajectory_items_v05_acute_daily_complete = Column(Integer, ForeignKey('status.status_id'))
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: text
    # Choices: N/A
    traj04wkenterdate = Column(String, nullable=False, comments=None)
    # 1. Please rate your chest pain by choosing the number that be...
    # Field Type: radio
    # Choices: 0, 0 No pain | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Pain as bad as you can imagine
    traj04worstpainscl = Column(Integer, nullable=False, comments=None)
    # 2. Please rate your chest pain by choosing the number that be...
    # Field Type: radio
    # Choices: 0, 0 No pain | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Pain as bad as you can imagine
    traj04avgpainscl = Column(Integer, nullable=False, comments=None)
    # 3. Please rate how much your chest pain has interfered with y...
    # Field Type: radio
    # Choices: 0, 0 Did not interfere | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Completely interfered
    traj04painintfactivscl = Column(Integer, nullable=False, comments=None)
    # Please rate the overall QUALITY of your SLEEP in the past 24 ...
    # Field Type: radio
    # Choices: 0, 0 Extremely poor | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Extremely good
    traj04sleepscl = Column(Integer, nullable=False, comments=None)
    # During the past 24 hours, how physically active were you?
    # Field Type: radio
    # Choices: 0, 0 Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Extremely
    traj04physactscl = Column(Integer, nullable=False, comments=None)
    # During the past 24 hours, how sad were you?
    # Field Type: radio
    # Choices: 0, 0 Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Extremely
    traj04sadscl = Column(Integer, nullable=False, comments=None)
    # During the past 24 hours, how angry were you?
    # Field Type: radio
    # Choices: 0, 0 Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Extremely
    traj04angryscl = Column(Integer, nullable=False, comments=None)
    # During the past 24 hours, how nervous were you?
    # Field Type: radio
    # Choices: 0, 0 Not at all | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10 Extremely
    traj04nervousscl = Column(Integer, nullable=False, comments=None)
    # During the past 24 hours, did you take any kind of medication...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj04medyn = Column(Boolean, nullable=False, comments=None)
    # Over-the-counter pain relievers (e.g., acetaminophen Tylenol,...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj04medlist1otc = Column(Boolean, nullable=False, comments=None)
    # Opioid pain relievers (e.g., oxycodone, Percocet, Nucynta, ta...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj04medlist2opioid = Column(Boolean, nullable=False, comments=None)
    # THC/CBD or marijuana products (edibles, gummies, CBD oil, wee...
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj04medlist3thc = Column(Boolean, nullable=False, comments=None)
    # Gabapentin or pregabalin (Neurontin, Lyrica, etc)
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj04medlist4gaba = Column(Boolean, nullable=False, comments=None)
    # Duloxetine (Cymbalta) or venlafaxine (Wellbutrin)
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj04medlist5dulox = Column(Boolean, nullable=False, comments=None)
    # Other, not specified above
    # Field Type: radio
    # Choices: Y, Yes | N, No
    traj04medlist6other = Column(Boolean, nullable=False, comments=None)
    # Please specify the other medication
    # Field Type: text
    # Choices: N/A
    traj04medlist6othertxt = Column(String, nullable=False, comments=None)