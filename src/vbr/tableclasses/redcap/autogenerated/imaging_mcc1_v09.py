"""Autogenerated 2021-11-05T05:03:30.465663 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcaptable import RcapTable
from ..rcconstants import REDCapConstants

__all__ = ["RcapImagingMcc1V09"]


class RcapImagingMcc1V09(RcapTable):
    """Imaging Mcc1 V09"""

    __redcap_form_name = "imaging_mcc1_v09"
    imaging_mcc1_v09_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    imaging_mcc1_v09_complete = Column(Integer, ForeignKey("status.status_id"))
    # Investigator initials
    # Field Type: text
    # Choices: N/A
    fmricuff_initials = Column(String, nullable=True, comments=None)
    # Verify Patient Name (as entered into scanner console):  Patie...
    # Field Type: text
    # Choices: N/A
    fmripatientname = Column(String, nullable=True, comments=None)
    # Cuff applied to R/L leg:(hint: MCC1: contralateral to surgica...
    # Field Type: radio
    # Choices: 1, Right | 2, Left
    fmricuffleg = Column(Integer, nullable=True, comments=None)
    # Re-calibration of pressure needed
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    fmricuffcontrarecal = Column(Boolean, nullable=True, comments=None)
    # Pressure 2
    # Field Type: text
    # Choices: N/A
    fmricuffcalfpressurerecal = Column(String, nullable=True, comments=None)
    # Pressure 2: (double entry)
    # Field Type: text
    # Choices: N/A
    fmricuffcalfpressurerecal2 = Column(String, nullable=True, comments=None)
    # Please enter technologist's quality rating for the T1 scan
    # Field Type: radio
    # Choices: 3, Green - good, Class 3 | 2, Yellow - borderline, Class 2 | 1, Red - unusable, Class 1
    fmricufft1techrating = Column(Integer, nullable=True, comments=None)
    # T1 scan repeated?
    # Field Type: yesno
    # Choices: N/A
    fmricufft1repeated = Column(Boolean, nullable=True, comments=None)
    # Please enter technologist's quality rating for the 2nd T1 scan
    # Field Type: radio
    # Choices: 3, Green - good, Class 3 | 2, Yellow - borderline, Class 2 | 1, Red - unusable, Class 1
    fmricufft1techrating2 = Column(Integer, nullable=True, comments=None)
    # Surgical site pain
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffrestpainss = Column(Numeric, nullable=True, comments=None)
    # Surgical site pain (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffrestpainss2 = Column(Numeric, nullable=True, comments=None)
    # Body pain
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffrestpainovrall = Column(Numeric, nullable=True, comments=None)
    # Body pain (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffrestpainovrall2 = Column(Numeric, nullable=True, comments=None)
    # Surgical site pain
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffcurrpainaftfirstscanss = Column(Numeric, nullable=True, comments=None)
    # Surgical site pain (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffcurrpainaftfirstscanss2 = Column(Numeric, nullable=True, comments=None)
    # Body pain
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffcurrpainaftfirstscanovrall = Column(Numeric, nullable=True, comments=None)
    # Body pain (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffcurrpainaftfirstscanovrall2 = Column(Numeric, nullable=True, comments=None)
    # Cuff pain
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffcurrpainaftfirstscancp = Column(Numeric, nullable=True, comments=None)
    # Cuff pain (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffcurrpainaftfirstscancp2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (beginning)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainbegin = Column(Numeric, nullable=True, comments=None)
    # cuff pain (beginning) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainbegin2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (middle)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainmid = Column(Numeric, nullable=True, comments=None)
    # cuff pain (middle) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainmid2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (end)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainend = Column(Numeric, nullable=True, comments=None)
    # cuff pain (end) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainend2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (beginning)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpaincpbegin = Column(Numeric, nullable=True, comments=None)
    # cuff pain (beginning) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpaincpbegin2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (middle)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpaincpmid = Column(Numeric, nullable=True, comments=None)
    # cuff pain (middle) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpaincpmid2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (end)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpaincpend = Column(Numeric, nullable=True, comments=None)
    # cuff pain (end) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpaincpend2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (beginning)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainrestscanbegin = Column(Numeric, nullable=True, comments=None)
    # cuff pain (beginning) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainrestscanbegin2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (middle)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainrestscanmid = Column(Numeric, nullable=True, comments=None)
    # cuff pain (middle) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainrestscanmid2 = Column(Numeric, nullable=True, comments=None)
    # cuff pain (end)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainrestscanend = Column(Numeric, nullable=True, comments=None)
    # cuff pain (end) (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainrestscanend2 = Column(Numeric, nullable=True, comments=None)
    # Surgical site pain
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainaftlastscanss = Column(Numeric, nullable=True, comments=None)
    # Surgical site pain (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainaftlastscanss2 = Column(Numeric, nullable=True, comments=None)
    # Body pain
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainaftlastscanany = Column(Numeric, nullable=True, comments=None)
    # Body pain (double entry)
    # Field Type: dropdown
    # Choices: 0.0, 0.0 | 0.5, 0.5 | 1.0, 1.0 | 1.5, 1.5 | 2.0, 2.0 | 2.5, 2.5 | 3.0, 3.0 | 3.5, 3.5 | 4.0, 4.0 | 4.5, 4.5 | 5.0, 5.0 | 5.5, 5.5 | 6.0, 6.0 | 6.5, 6.5 | 7.0, 7.0 | 7.5, 7.5 | 8.0, 8.0 | 8.5, 8.5 | 9.0, 9.0 | 9.5, 9.5 | 10.0, 10.0
    fmricuffpainaftlastscanany2 = Column(Numeric, nullable=True, comments=None)
    # Test Completed
    # Field Type: radio
    # Choices: 1, Yes, all scans were completed | 2, Yes, but only the scans indicated below were completed | 0, No, no scans were completed (add reason(s) to notes below)
    fmricuffcompletescl = Column(Integer, nullable=True, comments=None)
    # T1
    # Field Type: yesno
    # Choices: N/A
    fmricufft1yn = Column(Boolean, nullable=True, comments=None)
    # DWI
    # Field Type: yesno
    # Choices: N/A
    fmricuffdwiyn = Column(Boolean, nullable=True, comments=None)
    # 1rst Resting state
    # Field Type: yesno
    # Choices: N/A
    fmricuffrest1yn = Column(Boolean, nullable=True, comments=None)
    # fMRI individualized pressure
    # Field Type: yesno
    # Choices: N/A
    fmricuffipyn = Column(Boolean, nullable=True, comments=None)
    # fMRI standard pressure
    # Field Type: yesno
    # Choices: N/A
    fmricuffcpyn = Column(Boolean, nullable=True, comments=None)
    # 2nd Resting state
    # Field Type: yesno
    # Choices: N/A
    fmricuffrest2yn = Column(Boolean, nullable=True, comments=None)
    # Dicom files uploaded to TACC
    # Field Type: yesno
    # Choices: N/A
    fmricuffdicuploaded = Column(Boolean, nullable=True, comments=None)
    # Upload date/time
    # Field Type: text
    # Choices: N/A
    fmricuffdicupdate = Column(String, nullable=True, comments=None)
