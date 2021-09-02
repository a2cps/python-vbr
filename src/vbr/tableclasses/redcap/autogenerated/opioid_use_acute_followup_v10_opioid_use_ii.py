"""Autogenerated 2021-09-02T13:30:49.019174 by redcap_classfiles.py
"""

from vbr.pgrest import *
from vbr.tableclasses import Constants
from vbr.pgrest.constraints import Signature

from ..rcconstants import REDCapConstants
from ..rcaptable import RcapTable

__all__ = ['RcapOpioidUseAcuteFollowupV10OpioidUseIi']


class RcapOpioidUseAcuteFollowupV10OpioidUseIi(RcapTable):
    """Opioid Use Acute Followup V10 Opioid Use Ii
    """
    __redcap_form_name = 'opioid_use_acute_followup_v10_opioid_use_ii'
    opioid_use_acute_followup_v10_opioid_use_ii_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    opioid_use_acute_followup_v10_opioid_use_ii_complete = Column(
        Integer, ForeignKey('status.status_id'))
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    opioiduseafuopds = Column(Boolean, nullable=False, comments=None)
    # Medication #1
    # Field Type: descriptive
    # Choices: N/A
    opioiduseafu_dt_1 = Column(String, nullable=False, comments=None)
    # What is the name of the opioid medication?
    # Field Type: radio
    # Choices: 1, Hydrocodone (Vicodin, Norco) | 2, Oxycodone (Percocet, Oxycontin) | 3, Codeine (Tylenol 3, Tylenol 4) | 4, Tramadol (Ultram, Ultracet) | 5, Hydromorphone (Dilaudid) | 6, Morphine (MS Contin, MS IR) | 7, Tapentadol (Nucynta) | 8, Methadone | 9, Fentanyl (Duragesic) | 10, Other
    opioiduseafudrug1nm = Column(Integer, nullable=False, comments=None)
    # What is the dose of your Hydrocodone (Vicodin, Norco)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 5mg / 325mg | 2, Tablets with acetaminophen - 7.5mg / 325mg | 3, Tablets with acetaminophen - 10mg / 325mg | 4, Liquid - 7.5mg/500mg per 15ml
    opioiduseafu_meddosehydroc1 = Column(Integer,
                                         nullable=False,
                                         comments=None)
    # What is the dose of your Oxycodone (Percocet, Oxycontin)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen | 2, - 2.5mg / 325mg | 3, - 5mg / 325mg | 4, - 7.5mg / 325mg | 5, - 10mg / 325mg | 6, ------------------------ | 7, Tablets immediate release | 8, - 5mg | 9, - 7.5mg | 10, - 10mg | 11, - 15mg | 12, - 20mg | 13, - 30mg | 14, ------------------------ | 15, Tablets extended release | 16, - 10mg | 17, - 15mg | 18, - 20mg | 19, - 30mg | 20, - 40mg | 21, - 60mg | 22, - 80mg | 23, ------------------------- | 24, Liquid - 5mg / 5ml
    opioiduseafu_meddoseoxy1 = Column(Integer, nullable=False, comments=None)
    # What is the dose of your Codeine (Tylenol 3, Tylenol 4)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 15mg / 300mg | 2, Tablets with acetaminophen - 30mg / 300mg | 3, Tablets with acetaminophen - 60mg / 300mg | 4, Liquid - 12mg / 120mg per 5ml | 5, Tylenol 3 | 6, Tylenol 4
    opioiduseafu_meddosecodeine1 = Column(Integer,
                                          nullable=False,
                                          comments=None)
    # What is the dose of your Tramadol (Ultram, Ultracet)?
    # Field Type: dropdown
    # Choices: 1, 50mg | 2, 100mg | 3, 150mg | 4, 200mg | 5, 300mg
    opioiduseafu_meddosetram1 = Column(Integer, nullable=False, comments=None)
    # What is the dose of your Hydromorphone (Dilaudid)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release - 2mg | 2, Tablets immediate release - 4mg | 3, Tablets immediate release - 8mg | 4, Tablets immediate release - 12mg | 5, Tablets immediate release - 16mg | 6, Tablets immediate release - 32mg | 7, Liquid - 5mg / 5ml
    opioiduseafu_meddosehydrom1 = Column(Integer,
                                         nullable=False,
                                         comments=None)
    # What is the dose of your Morphine (MS Contin, MS IR)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 15mg | 3, - 30mg | 4, ------------------------------------- | 5, Tablets extended release | 6, - 15mg | 7, - 30mg | 8, - 60mg | 9, - 100mg | 10, - 200mg | 11, ------------------------------- | 12, Liquid - 10mg / 5ml
    opioiduseafu_meddosemorph1 = Column(Integer, nullable=False, comments=None)
    # What is the dose of your Tapentadol (Nucynta)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 50mg | 3, - 75mg | 4, - 100mg | 5, -------------------------------------- | 6, Tablets extended release | 7, - 50mg | 8, - 100mg | 9, - 150mg | 10, - 200mg | 11, - 250mg
    opioiduseafu_meddosetapen1 = Column(Integer, nullable=False, comments=None)
    # What is the dose of your Methadone?
    # Field Type: dropdown
    # Choices: 1, Tablets - 5mg | 2, Tablets - 10mg | 3, Liquid - 10mg/ml
    opioiduseafu_meddosemetha1 = Column(Integer, nullable=False, comments=None)
    # What is the dose of your Fentanyl (Duragesic)?
    # Field Type: dropdown
    # Choices: 1, Patch - 12mcg | 2, Patch - 25mcg | 3, Patch - 50mcg | 4, Patch - 75mcg | 5, Patch - 100mcg
    opioiduseafu_meddosefenta1 = Column(Integer, nullable=False, comments=None)
    # Over the past week, how many pills did you take in total?
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug1quanta = Column(String, nullable=False, comments=None)
    # Over the past week, how many teaspoons (1 teaspoon = 5 mL) di...
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug1quantb = Column(String, nullable=False, comments=None)
    # Over the past week, how many patches did you apply?
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug1quantc = Column(String, nullable=False, comments=None)
    # 1.a The name of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioiduseafuotherdrug1nm = Column(String, nullable=False, comments=None)
    # 1.b The dose of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioiduseafudose_oth1 = Column(String, nullable=False, comments=None)
    # Are you currently taking other opioid pain medications?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    opioiduseafud1other = Column(Boolean, nullable=False, comments=None)
    # Medication #2
    # Field Type: descriptive
    # Choices: N/A
    opioiduseafu_dt_2 = Column(String, nullable=False, comments=None)
    # 2 What is the name of the opioid medication?
    # Field Type: radio
    # Choices: 1, Hydrocodone (Vicodin, Norco) | 2, Oxycodone (Percocet, Oxycontin) | 3, Codeine (Tylenol 3, Tylenol 4) | 4, Tramadol (Ultram, Ultracet) | 5, Hydromorphone (Dilaudid) | 6, Morphine (MS Contin, MS IR) | 7, Tapentadol (Nucynta) | 8, Methadone | 9, Fentanyl (Duragesic) | 10, Other
    opioiduseafudrug2nm = Column(Integer, nullable=False, comments=None)
    # 2 What is the dose of your Hydrocodone (Vicodin, Norco)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 5mg / 325mg | 2, Tablets with acetaminophen - 7.5mg / 325mg | 3, Tablets with acetaminophen - 10mg / 325mg | 4, Liquid - 7.5mg/500mg per 15ml
    opioiduseafu_meddosehydroc2 = Column(Integer,
                                         nullable=False,
                                         comments=None)
    # 2 What is the dose of your Oxycodone (Percocet, Oxycontin)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen | 2, - 2.5mg / 325mg | 3, - 5mg / 325mg | 4, - 7.5mg / 325mg | 5, - 10mg / 325mg | 6, ------------------------ | 7, Tablets immediate release | 8, - 5mg | 9, - 7.5mg | 10, - 10mg | 11, - 15mg | 12, - 20mg | 13, - 30mg | 14, ------------------------ | 15, Tablets extended release | 16, - 10mg | 17, - 15mg | 18, - 20mg | 19, - 30mg | 20, - 40mg | 21, - 60mg | 22, - 80mg | 23, ------------------------- | 24, Liquid - 5mg / 5ml
    opioiduseafu_meddoseoxy2 = Column(Integer, nullable=False, comments=None)
    # 2 What is the dose of your Codeine (Tylenol 3, Tylenol 4)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 15mg / 300mg | 2, Tablets with acetaminophen - 30mg / 300mg | 3, Tablets with acetaminophen - 60mg / 300mg | 4, Liquid - 12mg / 120mg per 5ml | 5, Tylenol 3 | 6, Tylenol 4
    opioiduseafu_meddosecodeine2 = Column(Integer,
                                          nullable=False,
                                          comments=None)
    # 2 What is the dose of your Tramadol (Ultram, Ultracet)?
    # Field Type: dropdown
    # Choices: 1, 50mg | 2, 100mg | 3, 150mg | 4, 200mg | 5, 300mg
    opioiduseafu_meddosetram2 = Column(Integer, nullable=False, comments=None)
    # 2 What is the dose of your Hydromorphone (Dilaudid)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release - 2mg | 2, Tablets immediate release - 4mg | 3, Tablets immediate release - 8mg | 4, Tablets immediate release - 12mg | 5, Tablets immediate release - 16mg | 6, Tablets immediate release - 32mg | 7, Liquid - 5mg / 5ml
    opioiduseafu_meddosehydrom2 = Column(Integer,
                                         nullable=False,
                                         comments=None)
    # 2 What is the dose of your Morphine (MS Contin, MS IR)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 15mg | 3, - 30mg | 4, ------------------------------------- | 5, Tablets extended release | 6, - 15mg | 7, - 30mg | 8, - 60mg | 9, - 100mg | 10, - 200mg | 11, ------------------------------- | 12, Liquid - 10mg / 5ml
    opioiduseafu_meddosemorph2 = Column(Integer, nullable=False, comments=None)
    # 2 What is the dose of your Tapentadol (Nucynta)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 50mg | 3, - 75mg | 4, - 100mg | 5, -------------------------------------- | 6, Tablets extended release | 7, - 50mg | 8, - 100mg | 9, - 150mg | 10, - 200mg | 11, - 250mg
    opioiduseafu_meddosetapen2 = Column(Integer, nullable=False, comments=None)
    # 2 What is the dose of your Methadone?
    # Field Type: dropdown
    # Choices: 1, Tablets - 5mg | 2, Tablets - 10mg | 3, Liquid - 10mg/ml
    opioiduseafu_meddosemetha2 = Column(Integer, nullable=False, comments=None)
    # 2 What is the dose of your Fentanyl (Duragesic)?
    # Field Type: dropdown
    # Choices: 1, Patch - 12mcg | 2, Patch - 25mcg | 3, Patch - 50mcg | 4, Patch - 75mcg | 5, Patch - 100mcg
    opioiduseafu_meddosefenta2 = Column(Integer, nullable=False, comments=None)
    # 2 Over the past week, how many pills did you take in total?
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug2quanta = Column(String, nullable=False, comments=None)
    # 2 Over the past week, how many teaspoons (1 teaspoon = 5 mL) ...
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug2quantb = Column(String, nullable=False, comments=None)
    # 2 Over the past week, how many patches did you apply?
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug2quantc = Column(String, nullable=False, comments=None)
    # 2.a The name of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioiduseafuotherdrug2nm = Column(String, nullable=False, comments=None)
    # 2.b The dose of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioiduseafudose_oth2 = Column(String, nullable=False, comments=None)
    # 2 Are you currently taking other opioid pain medications?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    opioiduseafud2other = Column(Boolean, nullable=False, comments=None)
    # Medication #3
    # Field Type: descriptive
    # Choices: N/A
    opioiduseafu_dt_3 = Column(String, nullable=False, comments=None)
    # 3 What is the name of the opioid medication?
    # Field Type: radio
    # Choices: 1, Hydrocodone (Vicodin, Norco) | 2, Oxycodone (Percocet, Oxycontin) | 3, Codeine (Tylenol 3, Tylenol 4) | 4, Tramadol (Ultram, Ultracet) | 5, Hydromorphone (Dilaudid) | 6, Morphine (MS Contin, MS IR) | 7, Tapentadol (Nucynta) | 8, Methadone | 9, Fentanyl (Duragesic) | 10, Other
    opioiduseafudrug3nm = Column(Integer, nullable=False, comments=None)
    # 3 What is the dose of your Hydrocodone (Vicodin, Norco)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 5mg / 325mg | 2, Tablets with acetaminophen - 7.5mg / 325mg | 3, Tablets with acetaminophen - 10mg / 325mg | 4, Liquid - 7.5mg/500mg per 15ml
    opioiduseafu_meddosehydroc3 = Column(Integer,
                                         nullable=False,
                                         comments=None)
    # 3 What is the dose of your Oxycodone (Percocet, Oxycontin)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen | 2, - 2.5mg / 325mg | 3, - 5mg / 325mg | 4, - 7.5mg / 325mg | 5, - 10mg / 325mg | 6, ------------------------ | 7, Tablets immediate release | 8, - 5mg | 9, - 7.5mg | 10, - 10mg | 11, - 15mg | 12, - 20mg | 13, - 30mg | 14, ------------------------ | 15, Tablets extended release | 16, - 10mg | 17, - 15mg | 18, - 20mg | 19, - 30mg | 20, - 40mg | 21, - 60mg | 22, - 80mg | 23, ------------------------- | 24, Liquid - 5mg / 5ml
    opioiduseafu_meddoseoxy3 = Column(Integer, nullable=False, comments=None)
    # 3 What is the dose of your Codeine (Tylenol 3, Tylenol 4)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 15mg / 300mg | 2, Tablets with acetaminophen - 30mg / 300mg | 3, Tablets with acetaminophen - 60mg / 300mg | 4, Liquid - 12mg / 120mg per 5ml | 5, Tylenol 3 | 6, Tylenol 4
    opioiduseafu_meddosecodeine3 = Column(Integer,
                                          nullable=False,
                                          comments=None)
    # 3 What is the dose of your Tramadol (Ultram, Ultracet)?
    # Field Type: dropdown
    # Choices: 1, 50mg | 2, 100mg | 3, 150mg | 4, 200mg | 5, 300mg
    opioiduseafu_meddosetram3 = Column(Integer, nullable=False, comments=None)
    # 3 What is the dose of your Hydromorphone (Dilaudid)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release - 2mg | 2, Tablets immediate release - 4mg | 3, Tablets immediate release - 8mg | 4, Tablets immediate release - 12mg | 5, Tablets immediate release - 16mg | 6, Tablets immediate release - 32mg | 7, Liquid - 5mg / 5ml
    opioiduseafu_meddosehydrom3 = Column(Integer,
                                         nullable=False,
                                         comments=None)
    # 3 What is the dose of your Morphine (MS Contin, MS IR)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 15mg | 3, - 30mg | 4, ------------------------------------- | 5, Tablets extended release | 6, - 15mg | 7, - 30mg | 8, - 60mg | 9, - 100mg | 10, - 200mg | 11, ------------------------------- | 12, Liquid - 10mg / 5ml
    opioiduseafu_meddosemorph3 = Column(Integer, nullable=False, comments=None)
    # 3 What is the dose of your Tapentadol (Nucynta)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 50mg | 3, - 75mg | 4, - 100mg | 5, -------------------------------------- | 6, Tablets extended release | 7, - 50mg | 8, - 100mg | 9, - 150mg | 10, - 200mg | 11, - 250mg
    opioiduseafu_meddosetapen3 = Column(Integer, nullable=False, comments=None)
    # 3 What is the dose of your Methadone?
    # Field Type: dropdown
    # Choices: 1, Tablets - 5mg | 2, Tablets - 10mg | 3, Liquid - 10mg/ml
    opioiduseafu_meddosemetha3 = Column(Integer, nullable=False, comments=None)
    # 3 What is the dose of your Fentanyl (Duragesic)?
    # Field Type: dropdown
    # Choices: 1, Patch - 12mcg | 2, Patch - 25mcg | 3, Patch - 50mcg | 4, Patch - 75mcg | 5, Patch - 100mcg
    opioiduseafu_meddosefenta3 = Column(Integer, nullable=False, comments=None)
    # 3 Over the past week, how many pills did you take in total?
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug3quanta = Column(String, nullable=False, comments=None)
    # 3 Over the past week, how many teaspoons (1 teaspoon = 5 mL) ...
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug3quantb = Column(String, nullable=False, comments=None)
    # 3 Over the past week, how many patches did you apply?
    # Field Type: text
    # Choices: N/A
    opioiduseafudrug3quantc = Column(String, nullable=False, comments=None)
    # 3.a The name of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioiduseafuotherdrug3nm = Column(String, nullable=False, comments=None)
    # 3.b The dose of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioiduseafudose_oth3 = Column(String, nullable=False, comments=None)
