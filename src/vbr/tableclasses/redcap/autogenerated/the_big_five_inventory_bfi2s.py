"""Autogenerated 2021-09-02T15:55:09.538303 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapTheBigFiveInventoryBfi2S']

class RcapTheBigFiveInventoryBfi2S(RcapTable):
    """The Big Five Inventory Bfi2S
    """
    __redcap_form_name = 'the_big_five_inventory_bfi2s'
    the_big_five_inventory_bfi2s_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    the_big_five_inventory_bfi2s_complete = Column(Integer, ForeignKey('status.status_id'))
    # Tends to be quiet
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2squietscl = Column(Integer, nullable=False, comments=None)
    # Is compassionate, has a soft heart
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2scompassionatescl = Column(Integer, nullable=False, comments=None)
    # Tends to be disorganized
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sdisorganizedscl = Column(Integer, nullable=False, comments=None)
    # Worries a lot
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sworriesscl = Column(Integer, nullable=False, comments=None)
    # Is fascinated by art, music, or literature
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sfascinatedscl = Column(Integer, nullable=False, comments=None)
    # Is dominant, acts as a leader
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sdominantscl = Column(Integer, nullable=False, comments=None)
    # Is sometimes rude to others
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2srudescl = Column(Integer, nullable=False, comments=None)
    # Has difficulty getting started on tasks
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sdifficultstartscl = Column(Integer, nullable=False, comments=None)
    # Tends to feel depressed, blue
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sdepressedscl = Column(Integer, nullable=False, comments=None)
    # Has little interest in abstract ideas
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sllittleinterestscl = Column(Integer, nullable=False, comments=None)
    # Is full of energy
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2senergyscl = Column(Integer, nullable=False, comments=None)
    # Assumes the best about people
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sassumingbestscl = Column(Integer, nullable=False, comments=None)
    # Is reliable, can always be counted on
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sreliablescl = Column(Integer, nullable=False, comments=None)
    # Is emotionally stable, not easily upset
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sstableemotionscl = Column(Integer, nullable=False, comments=None)
    # Is original, comes up with new ideas
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2soriginalscl = Column(Integer, nullable=False, comments=None)
    # Is outgoing, sociable
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2soutgoingscl = Column(Integer, nullable=False, comments=None)
    # Can be cold and uncaring
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2suncaringscl = Column(Integer, nullable=False, comments=None)
    # Keeps things neat and tidy
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2stidyscl = Column(Integer, nullable=False, comments=None)
    # Is relaxed, handles stress well
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2srelaxedscl = Column(Integer, nullable=False, comments=None)
    # Has few artistic interests
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sfewartinterestscl = Column(Integer, nullable=False, comments=None)
    # Prefers to have others take charge
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2stakechargescl = Column(Integer, nullable=False, comments=None)
    # Is respectful, treats others with respect
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2srespectfulscl = Column(Integer, nullable=False, comments=None)
    # Is persistent, works until the task is finished
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2spersistentscl = Column(Integer, nullable=False, comments=None)
    # Feels secure, comfortable with self
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2ssecurescl = Column(Integer, nullable=False, comments=None)
    # Is complex, a deep thinker
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sthinkerscl = Column(Integer, nullable=False, comments=None)
    # Is less active than other people
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2slessactivescl = Column(Integer, nullable=False, comments=None)
    # Tends to find fault with others
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2sfaultwithothersscl = Column(Integer, nullable=False, comments=None)
    # Can be somewhat careless
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2scarelessscl = Column(Integer, nullable=False, comments=None)
    # Is temperamental, gets emotional easily
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2stemperamentalscl = Column(Integer, nullable=False, comments=None)
    # Has little creativity
    # Field Type: radio
    # Choices: 1, Disagree strongly | 2, Disagree a little | 3, Neutral | 4, Agree a little | 5, Agree strongly
    bfi2slittlecreativityscl = Column(Integer, nullable=False, comments=None)