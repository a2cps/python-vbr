# Defines classes for building A2CPS VBR tables for EHR data streams
# Utilizes TAPIS V3 (pgrest) and code developed by M. Vaughn for constructing single tables for A2CPS
# Adds the following common fields: project_id, protocol_id (maps to REDCap event_name), organization_id, creation_time, and last_updated_ts    

from ast import Num
from vbr.pgrest.constraints import Signature

from ..pgrest import *
from .constants import Constants
from .vbr_table import TableVBR

class EhrPatientDemographic(TableVBR):
  """EHR clinical and case characteristics (one per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  height_ehr = Column(Numeric, comments="In meters", nullable=True)
  weight_ehr = Column(Numeric, comments="In kg", nullable=True)  
  bmi_ehr = Column(Numeric, nullable=True)
  proc_name = Column(String, nullable=True)
  cpt_code = Column(String, nullable=True)
  age_ehr = Column(Integer, nullable=True)  
  los_ehr = Column(Integer, nullable=True)
  sex_ehr = Column(String, comments="M for male or F for female", nullable=True)
  surgeon = Column(String, nullable=True)
  icu_admit = Column(String, comments="Y or N",nullable=True)
  discharge_disposition = Column(String, nullable=True)
  duration_surgery = Column(Integer, comments="Defined in minutes", nullable=True)
  duration_anesthesia = Column(Integer, comments="In minutes", nullable=True)
  recovery_stay = Column(Integer, comments="In minutes", nullable=True)
  preop_sys_bp = Column(Integer, comments="Preoperative systolic blood pressure in mmHg", nullable=True)
  preop_dia_bp = Column(Integer, comments="Preoperative diastolic blood pressure in mmHg", nullable=True)
  recovery_sys_bp = Column(Integer, comments="Recovery room systolic blood pressure in mmHg", nullable=True)
  recovery_dia_bp = Column(Integer, comments="Recovery room diastolic blood pressure in mmHg", nullable=True)
  asa_ps = Column(Integer, comments="American Association of Anesthesia physical status 1-4", nullable=True)
  anethesia_type = Column(String, nullable=True)
  tourniquet_time = Column(Integer, comments="In minutes", nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 
    
class EhrImplants(TableVBR):
  """EHR implants (many per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True) 
  implant = Column(String, nullable=True)
  implant_manufacturer = Column(String, nullable=True)
  implant_model = Column(String, nullable=True)
  implant_area = Column(String, nullable=True)
  implant_laterality = Column(String, nullable=True)
  implant_number = Column(Integer, comments="number of implants used", nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True)   

class EhrMedicalHistory(TableVBR):
  """EHR medical history (many per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  pmh_diagnosis = Column(String, nullable=True)
  icd10_code = Column(String, nullable=True)
  icd9_code = Column(String, nullable=True)
  pmh_prior_surgery = Column(Integer, comments="duration from diagnosis to surgery in months", nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 
  
class EhrMedicationHistory(TableVBR):
  """EHR medication history (many per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  preop_medication = Column(String, nullable=True)
  medication_strength = Column(String, nullable=True)
  frequency_administration = Column(String, nullable=True)
  full_prescription = Column(String, nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 
  
class EhrSurgeryHistory(TableVBR):
  """EHR surgical history (many per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  surg_proc_name = Column(String, nullable=True)
  surgical_code = Column(String, nullable=True)
  proc_prior_surgery = Column(String, comments="months between surgery date and prior surgery", nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 
  
class EhrIntraoperativeMedication(TableVBR):
  """EHR intraoperative medication(many per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  med_name_intraop = Column(String, nullable=True)
  dose_med_intraop = Column(String, nullable=True)
  units_med_intraop = Column(String, nullable=True)
  mme_med_intraop = Column (Numeric, nullable=True)
  time_med_intraop = Column(Integer, comments="minutes between medication administration and moving to room", nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 
  
class EhrPainAssessments(TableVBR):
  """EHR pain assessments (many per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  pain_score = Column(Integer, comments="scale of 0 to 10", nullable=True)
  min_since_postop_time = Column (Integer, nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 

class EhrPostoperativeMedication(TableVBR):
  """EHR postoperative medication(many per subject) as defined by Rush""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  med_name_postop = Column(String, nullable=True)
  dose_med_postop = Column(String, nullable=True)
  units_med_postop = Column(String, nullable=True)
  mme_med_postop = Column (Numeric, nullable=True)
  time_med_postop = Column(Integer, comments="minutes between medication administration and moving to room", nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 

class EhrClinicalLaboratory(TableVBR):
  """EHR Clinical Laboratory tests and results (many per subject)""" 
  persistent_id = Column(String, comments="GUID assigned to subject", unique=True)
  loinc_id = Column(String, comments="Logical Observation Identifiers Names and Codes (LOINC)", nullable=True)
  lab_name = Column(String, comments="Common name of laboratory variable (e.g. glucose, sodium, potassium)", nullable=True)
  lab_day_surgery = Column(Integer, comments="Days between laboratory date and date of surgery. Anticipated range is -30 to +30.", nullable=True)
  lab_result = Column(Numeric, comments="Value of reported result contained in EPIC", nullable=True)
  lab_units = Column(String, comments="Units of the lab result (e.g. mg/dl)", nullable=True)
  lab_unit_high = Column(Numeric, comments="Upper range of reference value", nullable=True)
  lab_unit_low = Column(Numeric, comments="Lower range of reference value", nullable=True)
  project_id = Column(Integer, ForeignKey("project.project_id"))
  protocol_id = Column(Integer, ForeignKey("protocol.protocol_id"), nullable=True)
  organization_id = Column(Integer, ForeignKey("organization.organization_id"), nullable=True)
  creation_time = Column(CreatedTimeStamp, comments="When the record was created", nullable=True)
  last_updated_ts = Column(CreatedTimeStamp, comments="When the record was last updated or exported", nullable=True) 
