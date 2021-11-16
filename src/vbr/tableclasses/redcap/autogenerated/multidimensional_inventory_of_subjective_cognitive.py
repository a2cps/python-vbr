"""Autogenerated 2021-11-16T11:37:36.478362 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapMultidimensionalInventoryOfSubjectiveCognitive"]


class RcapMultidimensionalInventoryOfSubjectiveCognitive(RcapTable):
    """Multidimensional Inventory Of Subjective Cognitive"""

    __redcap_form_name = "multidimensional_inventory_of_subjective_cognitive"
    multidimensional_inventory_of_subjective_cognitive_id = (
        Constants.SERIAL_PRIMARY_KEY_COLUMN
    )
    multidimensional_inventory_of_subjective_cognitive_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # I have been able to think clearly without extra effort.
    # Field Type: radio
    # Choices: 1, Not at all | 2, A little bit | 3, Somewhat | 4, Quite a bit | 5, Very much
    miscithinkclrscl = Column(Integer, nullable=True, comments=None)
    # My mind has been sharp as usual.
    # Field Type: radio
    # Choices: 1, Not at all | 2, A little bit | 3, Somewhat | 4, Quite a bit | 5, Very much
    miscimindsharpscl = Column(Integer, nullable=True, comments=None)
    # I have been able to remember things as easily as usual withou...
    # Field Type: radio
    # Choices: 1, Not at all | 2, A little bit | 3, Somewhat | 4, Quite a bit | 5, Very much
    miscirememberscl = Column(Integer, nullable=True, comments=None)
    # I have been able to learn new things easily, like telephone n...
    # Field Type: radio
    # Choices: 1, Not at all | 2, A little bit | 3, Somewhat | 4, Quite a bit | 5, Very much
    miscilearnscl = Column(Integer, nullable=True, comments=None)
    # My ability to concentrate has been good.
    # Field Type: radio
    # Choices: 1, Not at all | 2, A little bit | 3, Somewhat | 4, Quite a bit | 5, Very much
    misciconcentratescl = Column(Integer, nullable=True, comments=None)
    # I have been able to keep track of what I was doing without ex...
    # Field Type: radio
    # Choices: 1, Not at all | 2, A little bit | 3, Somewhat | 4, Quite a bit | 5, Very much
    misciattentionscl = Column(Integer, nullable=True, comments=None)
    # I have had trouble shifting back and forth between different ...
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Very often
    miscishiftactivscl = Column(Integer, nullable=True, comments=None)
    # I had trouble planning out the steps of a task.
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Very often
    misciplanningscl = Column(Integer, nullable=True, comments=None)
    # I have had to work harder than usual to express myself clearly.
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Very often
    misciexpressscl = Column(Integer, nullable=True, comments=None)
    # I have had trouble finding the right word(s) to express myself.
    # Field Type: radio
    # Choices: 1, Never | 2, Rarely | 3, Sometimes | 4, Often | 5, Very often
    miscirightwordsscl = Column(Integer, nullable=True, comments=None)
