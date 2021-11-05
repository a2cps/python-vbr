"""Autogenerated 2021-11-05T15:48:31.886032 by redcap_classfiles.py
"""

from ....pgrest import *
from ...constants import Constants
from ..rcaptable import RcapTable
from ..rcconstants import REDCapConstants

__all__ = ["RcapOpioidUseBaselineV10OpioidUseI"]


class RcapOpioidUseBaselineV10OpioidUseI(RcapTable):
    """Opioid Use Baseline V10 Opioid Use I"""

    __redcap_form_name = "opioid_use_baseline_v10_opioid_use_i"
    opioid_use_baseline_v10_opioid_use_i_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    opioid_use_baseline_v10_opioid_use_i_complete = Column(
        Integer, ForeignKey("status.status_id")
    )
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 0, No | 1, Yes
    opioidusebslnopds = Column(Boolean, nullable=True, comments=None)
    # Ignored multiline Field Name in Data Dictionary
    # Field Type: radio
    # Choices: 1, Never taken an opioid before | 2, I have used an opioid in the past but never continuously | 3, 3 months-1 year | 4, >1year
    opioidusebslnexprncopd = Column(Integer, nullable=True, comments=None)
    # When is the last time you took an opioid?
    # Field Type: radio
    # Choices: 1, Within the last 3 months | 2, 3 months-1 year | 3, >1year
    opioidusebslnlsttmopd = Column(Integer, nullable=True, comments=None)
    # What is the name of the opioid medication?
    # Field Type: radio
    # Choices: 1, Hydrocodone (Vicodin, Norco) | 2, Oxycodone (Percocet, Oxycontin) | 3, Codeine (Tylenol 3, Tylenol 4) | 4, Tramadol (Ultram, Ultracet) | 5, Hydromorphone (Dilaudid) | 6, Morphine (MS Contin, MS IR) | 7, Tapentadol (Nucynta) | 8, Methadone | 9, Fentanyl (Duragesic) | 10, Other
    opioidusebslndrug1nm = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Hydrocodone (Vicodin, Norco)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 5mg / 325mg | 2, Tablets with acetaminophen - 7.5mg / 325mg | 3, Tablets with acetaminophen - 10mg / 325mg | 4, Liquid - 7.5mg/500mg per 15ml
    opioidusebsln_meddosehydroc1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Oxycodone (Percocet, Oxycontin)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen | 2, - 2.5mg / 325mg | 3, - 5mg / 325mg | 4, - 7.5mg / 325mg | 5, - 10mg / 325mg | 6, ------------------------ | 7, Tablets immediate release | 8, - 5mg | 9, - 7.5mg | 10, - 10mg | 11, - 15mg | 12, - 20mg | 13, - 30mg | 14, ------------------------ | 15, Tablets extended release | 16, - 10mg | 17, - 15mg | 18, - 20mg | 19, - 30mg | 20, - 40mg | 21, - 60mg | 22, - 80mg | 23, ------------------------- | 24, Liquid - 5mg / 5ml
    opioidusebsln_meddoseoxy1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Codeine (Tylenol 3, Tylenol 4)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 15mg / 300mg | 2, Tablets with acetaminophen - 30mg / 300mg | 3, Tablets with acetaminophen - 60mg / 300mg | 4, Liquid - 12mg / 120mg per 5ml | 5, Tylenol 3 | 6, Tylenol 4
    opioidusebsln_meddosecodeine1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Tramadol (Ultram, Ultracet)?
    # Field Type: dropdown
    # Choices: 1, 50mg | 2, 100mg | 3, 150mg | 4, 200mg | 5, 300mg
    opioidusebsln_meddosetram1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Hydromorphone (Dilaudid)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release - 2mg | 2, Tablets immediate release - 4mg | 3, Tablets immediate release - 8mg | 4, Tablets immediate release - 12mg | 5, Tablets immediate release - 16mg | 6, Tablets immediate release - 32mg | 7, Liquid - 5mg / 5ml
    opioidusebsln_meddosehydrom1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Morphine (MS Contin, MS IR)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 15mg | 3, - 30mg | 4, ------------------------------------- | 5, Tablets extended release | 6, - 15mg | 7, - 30mg | 8, - 60mg | 9, - 100mg | 10, - 200mg | 11, ------------------------------- | 12, Liquid - 10mg / 5ml
    opioidusebsln_meddosemorph1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Tapentadol (Nucynta)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 50mg | 3, - 75mg | 4, - 100mg | 5, -------------------------------------- | 6, Tablets extended release | 7, - 50mg | 8, - 100mg | 9, - 150mg | 10, - 200mg | 11, - 250mg
    opioidusebsln_meddosetapen1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Methadone?
    # Field Type: dropdown
    # Choices: 1, Tablets - 5mg | 2, Tablets - 10mg | 3, Liquid - 10mg/ml
    opioidusebsln_meddosemetha1 = Column(Integer, nullable=True, comments=None)
    # What is the dose of your Fentanyl (Duragesic)?
    # Field Type: dropdown
    # Choices: 1, Patch - 12mcg | 2, Patch - 25mcg | 3, Patch - 50mcg | 4, Patch - 75mcg | 5, Patch - 100mcg
    opioidusebsln_meddosefenta1 = Column(Integer, nullable=True, comments=None)
    # Over the past week, how many pills did you take per day on av...
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug1quanta = Column(String, nullable=True, comments=None)
    # Over the past week, how many teaspoons (1 teaspoon = 5 mL) di...
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug1quantb = Column(String, nullable=True, comments=None)
    # Over the past week, how many patches did you apply?
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug1quantc = Column(String, nullable=True, comments=None)
    # 1.a The name of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioidusebslnotherdrug1nm = Column(String, nullable=True, comments=None)
    # 1.b The dose of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioidusebslndose_oth1 = Column(String, nullable=True, comments=None)
    # Are you currently taking other opioid pain medications?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    opioidusebslnd1other = Column(Boolean, nullable=True, comments=None)
    # 2 What is the name of the opioid medication?
    # Field Type: radio
    # Choices: 1, Hydrocodone (Vicodin, Norco) | 2, Oxycodone (Percocet, Oxycontin) | 3, Codeine (Tylenol 3, Tylenol 4) | 4, Tramadol (Ultram, Ultracet) | 5, Hydromorphone (Dilaudid) | 6, Morphine (MS Contin, MS IR) | 7, Tapentadol (Nucynta) | 8, Methadone | 9, Fentanyl (Duragesic) | 10, Other
    opioidusebslndrug2nm = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Hydrocodone (Vicodin, Norco)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 5mg / 325mg | 2, Tablets with acetaminophen - 7.5mg / 325mg | 3, Tablets with acetaminophen - 10mg / 325mg | 4, Liquid - 7.5mg/500mg per 15ml
    opioidusebsln_meddosehydroc2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Oxycodone (Percocet, Oxycontin)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen | 2, - 2.5mg / 325mg | 3, - 5mg / 325mg | 4, - 7.5mg / 325mg | 5, - 10mg / 325mg | 6, ------------------------ | 7, Tablets immediate release | 8, - 5mg | 9, - 7.5mg | 10, - 10mg | 11, - 15mg | 12, - 20mg | 13, - 30mg | 14, ------------------------ | 15, Tablets extended release | 16, - 10mg | 17, - 15mg | 18, - 20mg | 19, - 30mg | 20, - 40mg | 21, - 60mg | 22, - 80mg | 23, ------------------------- | 24, Liquid - 5mg / 5ml
    opioidusebsln_meddoseoxy2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Codeine (Tylenol 3, Tylenol 4)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 15mg / 300mg | 2, Tablets with acetaminophen - 30mg / 300mg | 3, Tablets with acetaminophen - 60mg / 300mg | 4, Liquid - 12mg / 120mg per 5ml | 5, Tylenol 3 | 6, Tylenol 4
    opioidusebsln_meddosecodeine2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Tramadol (Ultram, Ultracet)?
    # Field Type: dropdown
    # Choices: 1, 50mg | 2, 100mg | 3, 150mg | 4, 200mg | 5, 300mg
    opioidusebsln_meddosetram2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Hydromorphone (Dilaudid)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release - 2mg | 2, Tablets immediate release - 4mg | 3, Tablets immediate release - 8mg | 4, Tablets immediate release - 12mg | 5, Tablets immediate release - 16mg | 6, Tablets immediate release - 32mg | 7, Liquid - 5mg / 5ml
    opioidusebsln_meddosehydrom2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Morphine (MS Contin, MS IR)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 15mg | 3, - 30mg | 4, ------------------------------------- | 5, Tablets extended release | 6, - 15mg | 7, - 30mg | 8, - 60mg | 9, - 100mg | 10, - 200mg | 11, ------------------------------- | 12, Liquid - 10mg / 5ml
    opioidusebsln_meddosemorph2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Tapentadol (Nucynta)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 50mg | 3, - 75mg | 4, - 100mg | 5, -------------------------------------- | 6, Tablets extended release | 7, - 50mg | 8, - 100mg | 9, - 150mg | 10, - 200mg | 11, - 250mg
    opioidusebsln_meddosetapen2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Methadone?
    # Field Type: dropdown
    # Choices: 1, Tablets - 5mg | 2, Tablets - 10mg | 3, Liquid - 10mg/ml
    opioidusebsln_meddosemetha2 = Column(Integer, nullable=True, comments=None)
    # 2 What is the dose of your Fentanyl (Duragesic)?
    # Field Type: dropdown
    # Choices: 1, Patch - 12mcg | 2, Patch - 25mcg | 3, Patch - 50mcg | 4, Patch - 75mcg | 5, Patch - 100mcg
    opioidusebsln_meddosefenta2 = Column(Integer, nullable=True, comments=None)
    # 2 Over the past week, how many pills did you take per day on ...
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug2quanta = Column(String, nullable=True, comments=None)
    # 2 Over the past week, how many teaspoons (1 teaspoon = 5 mL) ...
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug2quantb = Column(String, nullable=True, comments=None)
    # 2 Over the past week, how many patches did you apply?
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug2quantc = Column(String, nullable=True, comments=None)
    # 2.a The name of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioidusebslnotherdrug2nm = Column(String, nullable=True, comments=None)
    # 2.b The dose of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioidusebslndose_oth2 = Column(String, nullable=True, comments=None)
    # 2 Are you currently taking other opioid pain medications?
    # Field Type: radio
    # Choices: 1, Yes | 0, No
    opioidusebslnd2other = Column(Boolean, nullable=True, comments=None)
    # 3 What is the name of the opioid medication?
    # Field Type: radio
    # Choices: 1, Hydrocodone (Vicodin, Norco) | 2, Oxycodone (Percocet, Oxycontin) | 3, Codeine (Tylenol 3, Tylenol 4) | 4, Tramadol (Ultram, Ultracet) | 5, Hydromorphone (Dilaudid) | 6, Morphine (MS Contin, MS IR) | 7, Tapentadol (Nucynta) | 8, Methadone | 9, Fentanyl (Duragesic) | 10, Other
    opioidusebslndrug3nm = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Hydrocodone (Vicodin, Norco)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 5mg / 325mg | 2, Tablets with acetaminophen - 7.5mg / 325mg | 3, Tablets with acetaminophen - 10mg / 325mg | 4, Liquid - 7.5mg/500mg per 15ml
    opioidusebsln_meddosehydroc3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Oxycodone (Percocet, Oxycontin)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen | 2, - 2.5mg / 325mg | 3, - 5mg / 325mg | 4, - 7.5mg / 325mg | 5, - 10mg / 325mg | 6, ------------------------ | 7, Tablets immediate release | 8, - 5mg | 9, - 7.5mg | 10, - 10mg | 11, - 15mg | 12, - 20mg | 13, - 30mg | 14, ------------------------ | 15, Tablets extended release | 16, - 10mg | 17, - 15mg | 18, - 20mg | 19, - 30mg | 20, - 40mg | 21, - 60mg | 22, - 80mg | 23, ------------------------- | 24, Liquid - 5mg / 5ml
    opioidusebsln_meddoseoxy3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Codeine (Tylenol 3, Tylenol 4)?
    # Field Type: dropdown
    # Choices: 1, Tablets with acetaminophen - 15mg / 300mg | 2, Tablets with acetaminophen - 30mg / 300mg | 3, Tablets with acetaminophen - 60mg / 300mg | 4, Liquid - 12mg / 120mg per 5ml | 5, Tylenol 3 | 6, Tylenol 4
    opioidusebsln_meddosecodeine3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Tramadol (Ultram, Ultracet)?
    # Field Type: dropdown
    # Choices: 1, 50mg | 2, 100mg | 3, 150mg | 4, 200mg | 5, 300mg
    opioidusebsln_meddosetram3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Hydromorphone (Dilaudid)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release - 2mg | 2, Tablets immediate release - 4mg | 3, Tablets immediate release - 8mg | 4, Tablets immediate release - 12mg | 5, Tablets immediate release - 16mg | 6, Tablets immediate release - 32mg | 7, Liquid - 5mg / 5ml
    opioidusebsln_meddosehydrom3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Morphine (MS Contin, MS IR)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 15mg | 3, - 30mg | 4, ------------------------------------- | 5, Tablets extended release | 6, - 15mg | 7, - 30mg | 8, - 60mg | 9, - 100mg | 10, - 200mg | 11, ------------------------------- | 12, Liquid - 10mg / 5ml
    opioidusebsln_meddosemorph3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Tapentadol (Nucynta)?
    # Field Type: dropdown
    # Choices: 1, Tablets immediate release | 2, - 50mg | 3, - 75mg | 4, - 100mg | 5, -------------------------------------- | 6, Tablets extended release | 7, - 50mg | 8, - 100mg | 9, - 150mg | 10, - 200mg | 11, - 250mg
    opioidusebsln_meddosetapen3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Methadone?
    # Field Type: dropdown
    # Choices: 1, Tablets - 5mg | 2, Tablets - 10mg | 3, Liquid - 10mg/ml
    opioidusebsln_meddosemetha3 = Column(Integer, nullable=True, comments=None)
    # 3 What is the dose of your Fentanyl (Duragesic)?
    # Field Type: dropdown
    # Choices: 1, Patch - 12mcg | 2, Patch - 25mcg | 3, Patch - 50mcg | 4, Patch - 75mcg | 5, Patch - 100mcg
    opioidusebsln_meddosefenta3 = Column(Integer, nullable=True, comments=None)
    # 3 Over the past week, how many pills did you take per day on ...
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug3quanta = Column(String, nullable=True, comments=None)
    # 3 Over the past week, how many teaspoons (1 teaspoon = 5 mL) ...
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug3quantb = Column(String, nullable=True, comments=None)
    # 3 Over the past week, how many patches did you apply?
    # Field Type: text
    # Choices: N/A
    opioidusebslndrug3quantc = Column(String, nullable=True, comments=None)
    # 3.a The name of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioidusebslnotherdrug3nm = Column(String, nullable=True, comments=None)
    # 3.b The dose of other opioid medication
    # Field Type: text
    # Choices: N/A
    opioidusebslndose_oth3 = Column(String, nullable=True, comments=None)
    # How long have you been taking any kind of opioid medication r...
    # Field Type: radio
    # Choices: 1, Within the last 3 months | 2, 3 months-1 year | 3, >1year
    opioidusebslndrtnopd = Column(Integer, nullable=True, comments=None)
