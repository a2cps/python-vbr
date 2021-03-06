"""Autogenerated 2021-11-16T11:37:36.501581 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapOpioidSideEffectsAndLikeabilityV03SideEffec"]


class RcapOpioidSideEffectsAndLikeabilityV03SideEffec(RcapTable):
    """Opioid Side Effects And Likeability V03 Side Effec"""

    __redcap_form_name = "opioid_side_effects_and_likeability_v03_side_effec"
    opioid_side_effects_and_likeability_v03_side_effec_id = (
        Constants.SERIAL_PRIMARY_KEY_COLUMN
    )
    opioid_side_effects_and_likeability_v03_side_effec_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: yesno
    # Choices: N/A
    oseltakeop7dyn = Column(Boolean, nullable=True, comments=None)
    # Nausea
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_nausea = Column(Integer, nullable=True, comments=None)
    # Vomiting
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_vomit = Column(Integer, nullable=True, comments=None)
    # Constipation
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_constipation = Column(Integer, nullable=True, comments=None)
    # Difficulty passing urine
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_urination = Column(Integer, nullable=True, comments=None)
    # Difficulty concentrating
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_concentrate = Column(Integer, nullable=True, comments=None)
    # Drowsiness
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_drowsiness = Column(Integer, nullable=True, comments=None)
    # Dizziness
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_dizziness = Column(Integer, nullable=True, comments=None)
    # Confusion
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_confusion = Column(Integer, nullable=True, comments=None)
    # Fatigue
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_fatigue = Column(Integer, nullable=True, comments=None)
    # Dry mouth
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_drymouth = Column(Integer, nullable=True, comments=None)
    # Headache
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_headache = Column(Integer, nullable=True, comments=None)
    # Over the past 7 days, to what extent have you felt the urge t...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    osel_urgetouse = Column(Integer, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, I felt/feel no effect from the drug(s) at all | 2, I think I felt/feel a mild effect, but I'm not sure | 3, I definitely felt/feel an effect, but it is not really strong | 4, I felt/feel a strong effect | 5, I felt/feel a very strong effect
    osel_opeffect = Column(Integer, nullable=True, comments=None)
    # A. I was moody
    # Field Type: radio
    # Choices: 1, True | 0, False
    osel_moody = Column(Boolean, nullable=True, comments=None)
    # B. I felt itchy
    # Field Type: radio
    # Choices: 1, True | 0, False
    osel_itchy = Column(Boolean, nullable=True, comments=None)
    # C. I would be happy all the time if I felt as I felt then.
    # Field Type: radio
    # Choices: 1, True | 0, False
    osel_happy = Column(Boolean, nullable=True, comments=None)
    # D. I felt more excited than dreamy.
    # Field Type: radio
    # Choices: 1, True | 0, False
    osel_dreamy = Column(Boolean, nullable=True, comments=None)
    # E. My memory seemed sharper to me than usual.
    # Field Type: radio
    # Choices: 1, True | 0, False
    osel_memsharper = Column(Boolean, nullable=True, comments=None)
