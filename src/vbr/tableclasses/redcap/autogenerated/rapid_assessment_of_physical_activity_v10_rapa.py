"""Autogenerated 2021-11-16T11:37:36.514671 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcconstants import REDCapConstants

from ..rcaptable import RcapTable

__all__ = ["RcapRapidAssessmentOfPhysicalActivityV10Rapa"]


class RcapRapidAssessmentOfPhysicalActivityV10Rapa(RcapTable):
    """Rapid Assessment Of Physical Activity V10 Rapa"""

    __redcap_form_name = "rapid_assessment_of_physical_activity_v10_rapa"
    rapid_assessment_of_physical_activity_v10_rapa_id = (
        Constants.SERIAL_PRIMARY_KEY_COLUMN
    )
    rapid_assessment_of_physical_activity_v10_rapa_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # I rarely or never do any physical activities. Does this accur...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_rarly = Column(Boolean, nullable=True, comments=None)
    # I do some light or moderate physical activities, but not ever...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_light = Column(Boolean, nullable=True, comments=None)
    # I do some light physical activity every week.  Does this accu...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_lightweekly = Column(Boolean, nullable=True, comments=None)
    # I do moderate physical activities every week, but less  than ...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_mod = Column(Boolean, nullable=True, comments=None)
    # I do vigorous physical activities every week, but less  than ...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_vig = Column(Boolean, nullable=True, comments=None)
    # I do 30 minutes or more a day of moderate physical  activitie...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_modweekly = Column(Boolean, nullable=True, comments=None)
    # I do 20 minutes or more a day of vigorous physical  activitie...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_vigweekly = Column(Boolean, nullable=True, comments=None)
    # I do activities to increase muscle strength, such as  lifting...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_strength = Column(Boolean, nullable=True, comments=None)
    # I do activities to improve flexibility, such as stretching  o...
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    rapa_flex = Column(Boolean, nullable=True, comments=None)
