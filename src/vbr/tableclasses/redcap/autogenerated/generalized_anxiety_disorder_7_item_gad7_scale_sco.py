"""Autogenerated 2021-11-16T11:37:36.460497 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapGeneralizedAnxietyDisorder7ItemGad7ScaleSco"]


class RcapGeneralizedAnxietyDisorder7ItemGad7ScaleSco(RcapTable):
    """Generalized Anxiety Disorder 7 Item Gad7 Scale Sco"""

    __redcap_form_name = "generalized_anxiety_disorder_7_item_gad7_scale_sco"
    generalized_anxiety_disorder_7_item_gad7_scale_sco_id = (
        Constants.SERIAL_PRIMARY_KEY_COLUMN
    )
    generalized_anxiety_disorder_7_item_gad7_scale_sco_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Feeling nervous, anxious, or on edge
    # Field Type: radio
    # Choices: 0, Not at all | 1, Several days | 2, Over half the days | 3, Nearly every day
    gad2feelnervscl = Column(Integer, nullable=True, comments=None)
    # Not being able to stop or control worrying
    # Field Type: radio
    # Choices: 0, Not at all | 1, Several days | 2, Over half the days | 3, Nearly every day
    gad2notstopwryscl = Column(Integer, nullable=True, comments=None)
    # Worrying too much about different things
    # Field Type: radio
    # Choices: 0, Not at all | 1, Several days | 2, Over half the days | 3, Nearly every day
    gad7wrytoomchscl = Column(Integer, nullable=True, comments=None)
    # Trouble relaxing
    # Field Type: radio
    # Choices: 0, Not at all | 1, Several days | 2, Over half the days | 3, Nearly every day
    gad7troubrelxscl = Column(Integer, nullable=True, comments=None)
    # Being so restless that it's hard to sit still
    # Field Type: radio
    # Choices: 0, Not at all | 1, Several days | 2, Over half the days | 3, Nearly every day
    gad7rstlessscl = Column(Integer, nullable=True, comments=None)
    # Becoming easily annoyed or irritable
    # Field Type: radio
    # Choices: 0, Not at all | 1, Several days | 2, Over half the days | 3, Nearly every day
    gad7easyannoyedscl = Column(Integer, nullable=True, comments=None)
    # Feeling afraid as if something awful might happen
    # Field Type: radio
    # Choices: 0, Not at all | 1, Several days | 2, Over half the days | 3, Nearly every day
    gad7feelafrdscl = Column(Integer, nullable=True, comments=None)
    # If you checked off any problems, how difficult have these mad...
    # Field Type: radio
    # Choices: 0, Not difficult at all | 1, Somewhat difficult | 2, Very difficult | 3, Extremely difficult
    gad7difficulttowork = Column(Integer, nullable=True, comments=None)
