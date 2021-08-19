# Classes for each of the REDCap instrument tables defined for A2cPS MCC1 Main.
# Additional variables tbd by Martin, Margaret and Ari may be added to each of the tables. 
# If we choose NOT to include variables other than status for an instrument, consider consolidating the status variables into a view similar to the REDCap project dashboard. 
# REDCap selectors do not have consistent definitions. Should we use separate tables for each REDCap selector variable or find a more efficient way to address?
# Maybe map labels to selector variables within a single "RCapSelector" table per REDCap project? 

class RCapConsentedParticipantInformation(Table):
    """The RedCap Blood Sample CRF (bcsp) instrument."""
    rcap_consented_participant_information_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject
    record_id = Column(String)
    # REDCap guid used as the persistent id for the subject    
    guid = Column(String)
    # REDCap-defined status for this instrument 0-2 where 0 = "incomplete", 1 = "partially complete", and 2 = "complete"
    consented_participant_information_complete = Column(Integer, ForeignKey("status.status_id"))

class RCapPostConsentStudyPlan(Table):
    """The RedCap Post Consent Study Plan CRF v06 instrument."""
    rcap_postconsent_study_plan_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
    # REDCap-defined status for this instrument 0-2 where 0 = "incomplete", 1 = "partially complete", and 2 = "complete"
    postconsent_study_plan_crf_v06_complete = Column(Integer, ForeignKey("status.status_id")) 
 	# Include other fields? (REDCap fields 12-38 tbd) 

class RCapPatientDemographicsBaseline(Table):    
    """The REDCap Patient Demographics Baseline v03 instrument."""
    rcap_patient_demographics_baseline_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	age = Column(Integer, nullable=True)
    # Sex at birth selector 1-4 where 1=?, 2=?, 3=?, and 4=? (recheck REDCap for allowed values)
	sex = Column(Integer, nullable=True)
    # Ethnic selector 1-4 where 1=?, 2=?, 3=?, and 4=? (recheck REDCap for allowed values)
	ethnic = Column(Integer, nullable=True)
    # Dem_race allows selection of multiple integer values 1-7 where 1=?, 2=?, 3=?, 4=?, 5=?, 6=?, 7=?. Propose treating as a string.
    dem_race = Column(String, nullable=True)
    # REDCap-defined status for this instrument 0-2 where 0 = "incomplete", 1 = "partially complete", and 2 = "complete"
	patient_demographics_baseline_v03_demographics_i_complete = Column(Integer, ForeignKey("status.status_id")) 

class RCapOtherPainTreatments(Table):     
    """The REDCap Other Pain Treatments v3 Instrument."""
    rcap_other_pain_treatments_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	other_pain_treatments_v3_other_treatments_complete = Column(Integer, ForeignKey("status.status_id")) 
	# Include other fields? (REDCap fields 48-54 tbd)

class RCapOtherMedicalSurgicalTreatments(Table):     
    """The REDCap Other Medical Surgical Treatments ii Instrument."""
    rcap_other_medical_surgical_treatments_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	other_medical_surgical_treatments_ii_complete = Column(Integer, ForeignKey("status.status_id")) 
	# Include other fields? (REDCap fields 56-82 tbd)

class RCapPatientGlobalImpressionOfChange(Table):     
    """The REDCap Patient Global Impression of Change (pgic) Instrument."""
    rcap_patient_global_impression_of_change_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
    # pgicsymptomchangestatval selector 0-6 where 0=?,1=?, 2=?, 3=?, 4=?, 5=? and 6=? (recheck REDCap for allowed values)
	pgicsymptomchangestatval = Column(Integer, nullable=True)    
    pgicsymptomchangestatval (84, integer selector 0-6)
    patient_global_impression_of_change_pgic_complete = Column(Integer, ForeignKey("status.status_id"))

class RCapBriefPainInventoryShortForm(Table):     
    """The REDCap Brief Pain Inventory Short Form (BPISF) v23 Instrument."""
    brief_pain_inventory_short_form_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	bpisf_the_brief_pain_inventory_v23_short_form_bpi_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 86-114 tbd)

class RCapSymptomSeverityIndex(Table):     
    """The REDCap Symptom Severity Index v10 Instrument."""
    symptom_severity_index_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	symptom_severity_index_v10_ssi_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 116-122 tbd)

class RCapPainDetectQuestionaire(Table):     
    """The REDCap Pain Detect Questionaire (PDQ) Instrument."""     
    pain_detect_questionaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	pain_detect_questionaire_pdq_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 124-133 tbd)
    
class RCapKneeInjuryOsteoarthritisOutcomeScore(Table):     
    """The REDCap Knee Injury Osteoarthritis Outcome Score (koos12) Instrument."""
	knee_injury_osteoarthritis_outcome_score_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
    knee_injury_osteoarthritis_outcome_score_koos12_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 135-154 tbd)

class RCapPromisSFPhysicalFunction(Table):     
    """The REDCap Promis SF v12 Physical Function 8b Instrument."""
    promis_sf_physical_function_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	promis_sf_v12_physical_function_8b_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 156-164 tbd)]

class RCapPromisSFSleepDisturbance(Table):     
    """The REDCap Promis SF v10 Sleep Disturbance 6a Instrument."""
    promis_sf_sleep_disturbance_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	promis_sf_v10_sleep_disturbance_6a_sleep_i_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 166-171)

class RCapPainSleepDuration(Table):     
    """The REDCap Pain Sleep Duration Sleep ii Instrument."""
    painsleep_duration_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	painsleep_duration_sleep_ii_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 173-176 tbd)

class RCapPromisSFFatigue(Table):     
    """The REDCap Promis SF v10 Fatigue 7a Instrument."""
    promis_sf_fatigue_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	promis_sf_v10_fatigue_7a_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 178-184 tbd)

class RCapGeneralizedAnxietyDisorder7ItemScale(Table):     
    """The REDCap Generalized Anxiety Disorder 7 Item (GAD7) Scale Instrument."""
    generalized_anxiety_disorder_7_item_scale_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	generalized_anxiety_disorder_7_item_gad7_scale_sco_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 186-198)

class RCapPatientHealthQuestionnaireDepressionScale(Table):     
    """The REDCap Patient Health Questionnaire Depression Scale (PHQ) Instrument."""
    patient_health_questionnaire_depression_scale__id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	patient_health_questionnaire_depression_scale_phq_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 200-209)
 
class RCapPainCatastophizingQuestionnaire(Table):     
    """The REDCap Pain Catastophizing Questionnaire (PCS6) Instrument."""
    pain_catastrophizing_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	pain_catastrophizing_questionnaire_pcs6_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 211-218 tbd)

class RCapFearAvoidanceBeliefsQuestionnaire(Table):     
    """The REDCap Fear Avoidance Beliefs Questionnaire v03 (FABQ) Instrument."""
    fearavoidance_beliefs_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	fearavoidance_beliefs_questionnaire_v03_fabq_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 220-224 tbd)

class RCapPainResilienceScale(Table):     
    """The REDCap Pain Resilience Scale (PRS) Instrument."""
    pain_resilience_scale_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	pain_resilience_scale_prs_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 226-243 tbd)

class RCapPromisSFEmotionalSupport(Table):     
    """The REDCap Promis SF v20 Emotional Support 6a Instrument."""
    promis_sf_emotional_support_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	promis_sf_v20_emotional_support_6a_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 245-251 tbd)

class RCapPromisSFInformationalSupport(Table):     
    """The REDCap Promis SF v20 Informational Support 6a Instrument."""
    promis_sf_informational_support_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	promis_sf_v20_informational_support_6a_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 253-259 tbd)
    
class RCapMultidimentionalInventoryOfSubjectiveCognitive(Table):     
    """The REDCap Multidimentional Inventory of Subjective Cognitive Instrument."""
    multidimentional_inventory_of_subjective_cognitive_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	multidimentional_inventory_of_subjective_cognitive_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 261-271 tbd)
 
class RCapAdverseChildhoodExperienceQuestionnaire(Table):     
    """The REDCap Adverse Childhood Experience Questionnaire (ACE) Instrument."""
    adverse_childhood_experience_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	adverse_childhood_experience_questionnaire_ace_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 273-285)
 
class RCapTaps1(Table):   
    """The REDCap Taps1 Instrument."""
    taps1_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	taps1_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 287-292 tbd)

class RCapTaps2(Table):   
    """The REDCap Taps1 Instrument."""
    taps2_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)    
	taps2_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 294-341)
 
class RCapOpiodUseBaseline(Table):   
    """The REDCap Opiod Use Baseline v10 Opiod Use i Instrument."""
    opioid_use_baseline_id  = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	opioid_use_baseline_v10_opioid_use_i_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 343-396 tbd)
 
class RCapOpiodUseAcuteFollowup(Table):   
    """The REDCap Opiod Use Acute Followup v10 Opiod Use ii Instrument."""
    opioid_use_acute_followup_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
    # Check REDCap to see id the "baseline" portion of the fieldname below has been corrected.
	opioid_use_baseline_v10_opioid_use_ii_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 398-448 tbd)
    
class RCapOpiodUseLongtermFollowup(Table):   
    """The REDCap Opiod Use Longterm Followup v10 Opiod Use iii Instrument."""
    opioid_use_longterm_followup_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	opioid_use_longterm_followup_v10_opioid_use_iii_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 450-500 tbd)
    
class RCapOpiodSideEffectsAndLikeability(Table):   
    """The REDCap Opiod Side Effects and Likeability v03 Instrument."""
    opioid_side_effects_and_likeability_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	opioid_side_effects_and_likeability_v03_side_effec_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 502-523 tbd)

class RCapOpiodAndPainControlSatisfaction(Table):   
    """The REDCap Opiod and Pain Control Satisfaction v02 Instrument."""
    opioid_and_pain_control_satisfaction_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	opioid_and_pain_control_satisfaction_v02_satisfact_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 525-527 tbd)

class RCapCurrentOpiodMisuse(Table):   
    """The REDCap Current Opiod Misuse v02 Instrument."""
    current_opioid_misuse_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	current_opioid_misuse_v02_comm_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 529-540 tbd)
    
class RCapRapidAssessmentOfPhysicalActivity(Table):   
    """The REDCap Rapid Assessment of Physical Activity (RAPA) v10 Instrument."""
    rapid_assessment_of_physical_activity_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	rapid_assessment_of_physical_activity_v10_rapa_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 542-554)]
    
class RCapGeneralSensorySensitivity(Table):   
    """The REDCap General Sensory Sensitivity v02 GSS8 Instrument."""
    general_sensory_sensitivity_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	general_sensory_sensitivity_v02_gss8_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 556-567 tbd)

class RCapTheBigFiveInventory(Table):   
    """The REDCap Big Five Inventory (BFI2S) Instrument."""
    the_big_five_inventory_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	the_big_five_inventory_bfi2s_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 569-599 tbd)

class RCapPatientDemographicsFullPart2(Table):   
    """The REDCap Patient Demographics Full Part 2 v03 Instrument."""
    patient_demographics_full_part_2_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)
	patient_demographics_full_part_2_v03_demographics_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 601-616 tbd)

class RCapSelfadministeredComorbidityQuestionnaire(Table):   
    """The REDCap Self-administered Comorbidity Questionnaire (SCQ) v4 Instrument."""
    selfadministered_comorbidity_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	selfadministered_comorbidity_questionnaire_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 618-661 tbd) 

class RCapExpectationItems(Table):   
    """The REDCap Expectation Items v12 Instrument."""
    expectation_items_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	expectation_items_v12_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 663-665 tbd)
    
class RCapAcutePhaseTrajectoryItems(Table):   
    """The REDCap Acute Phase Trajectory Items v05 Instrument."""
    acute_phase_trajectory_items_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	acute_phase_trajectory_items_v05_acute_daily_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 667-684 tbd)

class RCapDailyItems6Mo(Table):   
    """The REDCap Daily Items 6 Month v03 Instrument."""
    daily_items_6_mo_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	daily_items_6_mo_v03_6month_daily_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 686-698 tbd)

class RCapMonth12Followup(Table):   
    """The REDCap Month 12 Remote Followup v20 Instrument."""
    month12_followup = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	month_remote_followup_v20_12month_followup_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 700-713 tbd)
 
class RCapFunctionalTesting(Table):   
    """The REDCap Functional Testing Instrument."""
    functional_testing_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	functional_testing_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 715-754 tbd)
    
class RCapQstMcc1(Table):   
    """The REDCap QST MCC1 v03 Instrument."""
    qst_mcc1_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	qst_mcc1_v03_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 756-837 tbd)

class RCapCurrentMedications(Table):   
    """The REDCap Current Medications v02 Instrument."""
    current_medications_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	current_medications_v02_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 839-843 tbd)

class RCapBloodSampleCRF(Table):
    """The RedCap Blood Sample CRF (bcsp) instrument."""
    rcap_blood_sample_crf_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID); another persistent_id may be needed for the biosample if the aliquot_brcd not persistent and unique. 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    bscp_hrs_since_water = Column(Integer, nullable=True)
    bscp_hrs_since_food = Column(Integer, nullable=True)
    bscp_hrs_since_cafstim = Column(Integer, nullable=True)
    # REDCap-defined (848)integer selector 1-3
	bscp_caff_cups_amt = Column(Integer, nullable=True)
    # REDCap-defined (849) 0-1 binary selector
	bscp_any_vacc = Column(Binary, nullable=True)
    # REDCap-defined (850) 0-1 binary selector   
	bscp_verify_pt = Column(Binary, nullable=True)
	bscp_ra_initials = Column(String, nullable=True)
	bscp_phleb_by_init = Column(String, nullable=True)
	bscp_sample_obtained = Column(Binary, nullable=True)
    # REDCap-defined (854)integer selector 1-5
	bscp_no_sample_reason(Integer, nullable=True)
	bscp_samplekit_brcd = Column(String, nullable=True)
    # Should use as biosample creation timestamp if not NULL AND timestamp < current
	bscp_time_blood_draw = Column(CreatedTimeStamp, nullable=True)
	bscp_dt1 = Column(String, nullable=True)
	bscp_lav1_not_obt = Column(Binary, nullable=True)
	bscp_lav1_brcd = Column(String, nullable=True)
	bscp_paxg_not_obt = Column(Binary, nullable=True)
	bscp_paxg_brcd  = Column(String, nullable=True)
	bscp_dt2  = Column(String, nullable=True)
	bscp_time_centrifuge = Column(Date, nullable=True)
	bscp_lav1_centrif_brcd = Column(String, nullable=True)
	bscp_plugcap_centrif_brcd = Column(String, nullable=True)
    # Correct syntax for numeric (5,2)?
	bscp_deg_of_hemolysis = Column (Numeric (5,2), nullable=True)
	bscp_dt_3 = Column(String, nullable=True)
	bscp_aliquot_box_brcd = Column(String, nullable=True)
	bscp_buffycoat_na = Column(Binary, nullable=True)
	bscp_buffycoat_brcd  = Column(String, nullable=True)
	bscp_plasma_brcd = Column(String, nullable=True)
	bscp_aliq_cnt = Column(Integer, nullable=True)
	bscp_paxg_box_brcd = Column(String, nullable=True)
	bscp_paxg_aliq_na = Column(Binary, nullable=True)
    bscp_paxg_aliq_brcd = Column(String, nullable=True)
    bscp_aliquot_freezer_time = Column(Date, nullable=True)
    bscp_dt_4 = Column(String, nullable=True)
    bscp_protocol_dev = Column(Binary, nullable=True)
    # REDCap-defined (879)integer selector 1-3
    bscp_protocol_dev_reason = Column(Integer, nullable=True)
    bscp_comments = Column(String, nullable=True)
    bscp_procby_initials = Column(String, nullable=True)
    # REDCap-defined (882)integer selector 0-2
	blood_sample_collection_and_processing_crf_complete = Column(Integer, nullable=True)

class RCapImagingItems(Table):
    """The RedCap Imaging Items v11 Instrument."""
    imaging_items_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	imaging_items_v11_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 883-890 tbd)
    
class RCapImagingMCC1(Table):
    """The RedCap Imaging MCC1 v09 Instrument."""
    imaging_mcc1_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	imaging_mcc1_v09_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 891-949 tbd)
    
class RCapStudyVisitFeedback(Table):
    """The RedCap Study Visit Feedback v03 Instrument."""
    study_visit_feedback_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	study_visit_feedback_v03_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 951-985 tbd)
    
class RCapPatientEncounters(Table):
    """The RedCap Patient Encounters Instrument."""
    patient_encounters_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	patient_encounters_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 987-990 tbd)
    
class RCapReportableEventDeviation(Table):
    """The RedCap Reportable Event Deviation v03 Instrument."""
    reportable_eventdeviation_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String) 
	reportable_eventdeviation_v03_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 992-1043 tbd)
    
class RCapEarlyWithdrawal(Table):
    """The RedCap Early Withdrawal v04 Instrument."""
    early_withdrawal_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID) 
    persistent_id = Constants.STRING_PERSISTENT_ID
    creation_time = Column(CreatedTimeStamp, nullable=True)
    # Get timestamp for last update; check if next code line is correct. 
    last_updated_ts = Column(UpdatedTimeStamp, nullable=True)
    # REDCap record_id identifying subject. Do we want to ETL these or JUST use the persistent subject_id (GUID)?
    record_id = Column(String)  
	early_withdrawal_v04_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (REDCap fields 1045-1051 tbd)

