"""Autogenerated 2021-10-15T10:45:47.676974 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapExpectationItemsV12']


class RcapExpectationItemsV12(RcapTable):
    """Expectation Items V12
    """
    __redcap_form_name = 'expectation_items_v12'
    expectation_items_v12_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    expectation_items_v12_complete = Column(Integer,
                                            ForeignKey('status.status_id'))
    # How much functional ability do you expect to have after you r...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    eor_funct_ability = Column(Integer, nullable=True, comments=None)
    # I expect that the pain related with this surgery will relieve...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    eor_surg_relieve_pain = Column(Integer, nullable=True, comments=None)
    # I'm afraid of pain or other complications during and/or after...
    # Field Type: radio
    # Choices: 0, 0 | 1, 1 | 2, 2 | 3, 3 | 4, 4 | 5, 5 | 6, 6 | 7, 7 | 8, 8 | 9, 9 | 10, 10
    eor_surg_relieve_pain_2 = Column(Integer, nullable=True, comments=None)
