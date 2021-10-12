"""Autogenerated 2021-10-12T09:26:27.483311 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapCurrentOpioidMisuseV02Comm']

class RcapCurrentOpioidMisuseV02Comm(RcapTable):
    """Current Opioid Misuse V02 Comm
    """
    __redcap_form_name = 'current_opioid_misuse_v02_comm'
    current_opioid_misuse_v02_comm_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    current_opioid_misuse_v02_comm_complete = Column(Integer, ForeignKey('status.status_id'))
    # 1. In the past 30 days, how often have you had to go to someo...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commothphyscmedpst30dyscl = Column(Integer, nullable=False, comments=None)
    # 2. In the past 30 days, how often have you taken your opioid ...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commtakmeddifpast30dayscl = Column(Integer, nullable=False, comments=None)
    # 3. In the past 30 days, how much of your time was spent think...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commopithkpast30dayscl = Column(Integer, nullable=False, comments=None)
    # 4. In the past 30 days, how often have you needed to take opi...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commsomelsmedpast30dayscl = Column(Integer, nullable=False, comments=None)
    # 5. In the past 30 days, how often have you been worried about...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commhanmedworpast30dayscl = Column(Integer, nullable=False, comments=None)
    # 6. In the past 30 days, how often have others been worried ab...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commothworrypast30dayscl = Column(Integer, nullable=False, comments=None)
    # 7. In the past 30 days, how often have you had to make an eme...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commemecalapppast30dayscl = Column(Integer, nullable=False, comments=None)
    # 8. In the past 30 days, how often have you had to take more o...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commtakmormedpast30dayscl = Column(Integer, nullable=False, comments=None)
    # 9. In the past 30 days, how often have you borrowed opioid pa...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commbormedpast30dayscl = Column(Integer, nullable=False, comments=None)
    # 10. In the past 30 days, how often have you used your opioid ...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commothsympast30dayscl = Column(Integer, nullable=False, comments=None)
    # 11. In the past 30 days, how often have you had to visit the ...
    # Field Type: radio
    # Choices: 0, Never | 1, Seldom | 2, Sometimes | 3, Often | 4, Very Often
    commemergrmpast30dayscl = Column(Integer, nullable=False, comments=None)