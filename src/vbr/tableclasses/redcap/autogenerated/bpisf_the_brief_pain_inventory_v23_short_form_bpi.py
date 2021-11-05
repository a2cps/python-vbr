"""Autogenerated 2021-11-05T05:03:30.338820 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcaptable import RcapTable
from ..rcconstants import REDCapConstants

__all__ = ["RcapBpisfTheBriefPainInventoryV23ShortFormBpi"]


class RcapBpisfTheBriefPainInventoryV23ShortFormBpi(RcapTable):
    """Bpisf The Brief Pain Inventory V23 Short Form Bpi"""

    __redcap_form_name = "bpisf_the_brief_pain_inventory_v23_short_form_bpi"
    bpisf_the_brief_pain_inventory_v23_short_form_bpi_id = (
        Constants.SERIAL_PRIMARY_KEY_COLUMN
    )
    bpisf_the_brief_pain_inventory_v23_short_form_bpi_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Field Name was empty in Data Dictionary
    # Field Type: text
    # Choices: N/A
    bpipainanatsiteareatxt = Column(String, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z1_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the head / face /...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z1_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z2_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the neck? Choose ...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z2_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z3_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the chest/breast?...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z3_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z4_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the abdomen / pel...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z4_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z5_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the RIGHT side: s...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z5_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z6_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the LEFT side: sh...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z6_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z7_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the  upper back /...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z7_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z8_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the RIGHT side: h...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z8_dur = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpi_mbm_z9_rate = Column(Integer, nullable=True, comments=None)
    # How long have you been experiencing pain in the LEFT side: hi...
    # Field Type: radio
    # Choices: 1, less than 1 month | 2, 1 month or more, but less than 6 months | 3, 6 months or more, but less than 2 years | 4, 2 years or more
    bpi_mbm_z9_dur = Column(Integer, nullable=True, comments=None)
    # Please rate your surgical site (chest) pain by choosing the n...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpiworstpainratingss = Column(Integer, nullable=True, comments=None)
    # Please rate any other pain (excluding surgical site) by choos...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    bpiworstpainratingexclss = Column(Integer, nullable=True, comments=None)
    # a. General Activity
    # Field Type: radio
    # Choices: 0, Does not interfere  0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Completely interferes  10
    bpipainintfrgnrlactvtyscl = Column(Integer, nullable=True, comments=None)
    # b. Mood
    # Field Type: radio
    # Choices: 0, Does not interfere  0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Completely interferes  10
    bpipainintfrmoodscl = Column(Integer, nullable=True, comments=None)
    # c. Walking ability
    # Field Type: radio
    # Choices: 0, Does not interfere  0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Completely interferes  10
    bpipainintfrwlkablscl = Column(Integer, nullable=True, comments=None)
    # d Normal work (includes both work outside the home and housew...
    # Field Type: radio
    # Choices: 0, Does not interfere  0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Completely interferes  10
    bpipainnrmlwrkintrfrscl = Column(Integer, nullable=True, comments=None)
    # e. Relations with other people
    # Field Type: radio
    # Choices: 0, Does not interfere  0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Completely interferes  10
    bpipainrelationsintrfrscl = Column(Integer, nullable=True, comments=None)
    # f. Sleep
    # Field Type: radio
    # Choices: 0, Does not interfere  0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Completely interferes  10
    bpipainsleepintrfrscl = Column(Integer, nullable=True, comments=None)
    # g. Enjoyment of life
    # Field Type: radio
    # Choices: 0, Does not interfere  0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, Completely interferes  10
    bpipainenjoymntintrfrscl = Column(Integer, nullable=True, comments=None)
