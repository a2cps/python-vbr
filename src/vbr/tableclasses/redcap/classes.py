from vbr.pgrest.constraints import Signature
from ...pgrest import *
from ..constants import Constants

from .rcconstants import REDCapConstants
from .rcaptable import RcapTable

# Classes for each of the Rcap instrument tables defined for A2cPS MCC1 Main.
# Additional variables tbd by Martin, Margaret and Ari may be added to each of the tables.
# If we choose NOT to include variables other than status for an instrument, consider consolidating the status variables into a view similar to the Rcap project dashboard.
# Rcap selectors do not have consistent definitions. Should we use separate tables for each Rcap selector variable or find a more efficient way to address?
# Maybe map labels to selector variables within a single "RcapSelector" table per Rcap project?


class RcapConsentedParticipantInformation(RcapTable):
    """The RedCap Blood Sample CRF (bcsp) instrument."""
    rcap_consented_participant_information_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    guid = REDCapConstants.GUID
    # Rcap-defined status for this instrument 0-2 where 0 = "incomplete", 1 = "partially complete", and 2 = "complete"
    consented_participant_information_complete = Column(
        Integer, ForeignKey("status.status_id"))


class RcapPostConsentStudyPlan(RcapTable):
    """The RedCap Post Consent Study Plan CRF v06 instrument."""
    rcap_postconsent_study_plan_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # Rcap-defined status for this instrument 0-2 where 0 = "incomplete", 1 = "partially complete", and 2 = "complete"
    postconsent_study_plan_crf_v06_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 12-38 tbd)


class RcapPatientDemographicsBaseline(RcapTable):
    """The Rcap Patient Demographics Baseline v03 instrument."""
    rcap_patient_demographics_baseline_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    age = Column(Integer, nullable=True)
    # Sex at birth selector 1-4 where 1=?, 2=?, 3=?, and 4=? (recheck Rcap for allowed values)
    sex = Column(Integer, nullable=True)
    # Ethnic selector 1-4 where 1=?, 2=?, 3=?, and 4=? (recheck Rcap for allowed values)
    ethnic = Column(Integer, nullable=True)
    # Dem_race allows selection of multiple integer values 1-7 where 1=?, 2=?, 3=?, 4=?, 5=?, 6=?, 7=?. Propose treating as a string.
    dem_race = Column(String, nullable=True)
    # Rcap-defined status for this instrument 0-2 where 0 = "incomplete", 1 = "partially complete", and 2 = "complete"
    patient_demographics_baseline_v03_demographics_i_complete = Column(
        Integer, ForeignKey("status.status_id"))


class RcapOtherPainTreatments(RcapTable):
    """The Rcap Other Pain Treatments v3 Instrument."""
    rcap_other_pain_treatments_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    other_pain_treatments_v3_other_treatments_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 48-54 tbd)


class RcapOtherMedicalSurgicalTreatments(RcapTable):
    """The Rcap Other Medical Surgical Treatments ii Instrument."""
    rcap_other_medical_surgical_treatments_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    #persistent_id (subject GUID)
    other_medical_surgical_treatments_ii_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 56-82 tbd)


class RcapPatientGlobalImpressionOfChange(RcapTable):
    """The Rcap Patient Global Impression of Change (pgic) Instrument."""
    rcap_patient_global_impression_of_change_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # pgicsymptomchangestatval selector 0-6 where 0=?,1=?, 2=?, 3=?, 4=?, 5=? and 6=? (recheck Rcap for allowed values)
    pgicsymptomchangestatval = Column(Integer, nullable=True)
    # pgicsymptomchangestatval (84, integer selector 0-6)
    patient_global_impression_of_change_pgic_complete = Column(
        Integer, ForeignKey("status.status_id"))


class RcapBriefPainInventoryShortForm(RcapTable):
    """The Rcap Brief Pain Inventory Short Form (BPISF) v23 Instrument."""
    brief_pain_inventory_short_form_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    bpisf_the_brief_pain_inventory_v23_short_form_bpi_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 86-114 tbd)


class RcapSymptomSeverityIndex(RcapTable):
    """The Rcap Symptom Severity Index v10 Instrument."""
    symptom_severity_index_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    symptom_severity_index_v10_ssi_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 116-122 tbd)


class RcapPainDetectQuestionaire(RcapTable):
    """The Rcap Pain Detect Questionaire (PDQ) Instrument."""
    pain_detect_questionaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    pain_detect_questionaire_pdq_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 124-133 tbd)


class RcapKneeInjuryOsteoarthritisOutcomeScore(RcapTable):
    """The Rcap Knee Injury Osteoarthritis Outcome Score (koos12) Instrument."""
    knee_injury_osteoarthritis_outcome_score_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    knee_injury_osteoarthritis_outcome_score_koos12_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 135-154 tbd)


class RcapPromisSFPhysicalFunction(RcapTable):
    """The Rcap Promis SF v12 Physical Function 8b Instrument."""
    promis_sf_physical_function_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    promis_sf_v12_physical_function_8b_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 156-164 tbd)]


class RcapPromisSFSleepDisturbance(RcapTable):
    """The Rcap Promis SF v10 Sleep Disturbance 6a Instrument."""
    promis_sf_sleep_disturbance_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    promis_sf_v10_sleep_disturbance_6a_sleep_i_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 166-171)


class RcapPainSleepDuration(RcapTable):
    """The Rcap Pain Sleep Duration Sleep ii Instrument."""
    painsleep_duration_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    painsleep_duration_sleep_ii_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 173-176 tbd)


class RcapPromisSFFatigue(RcapTable):
    """The Rcap Promis SF v10 Fatigue 7a Instrument."""
    promis_sf_fatigue_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    promis_sf_v10_fatigue_7a_complete = Column(Integer,
                                               ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 178-184 tbd)


class RcapGeneralizedAnxietyDisorder7ItemScale(RcapTable):
    """The Rcap Generalized Anxiety Disorder 7 Item (GAD7) Scale Instrument."""
    generalized_anxiety_disorder_7_item_scale_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    generalized_anxiety_disorder_7_item_gad7_scale_sco_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 186-198)


class RcapPatientHealthQuestionnaireDepressionScale(RcapTable):
    """The Rcap Patient Health Questionnaire Depression Scale (PHQ) Instrument."""
    patient_health_questionnaire_depression_scale__id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    patient_health_questionnaire_depression_scale_phq_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 200-209)


class RcapPainCatastophizingQuestionnaire(RcapTable):
    """The Rcap Pain Catastophizing Questionnaire (PCS6) Instrument."""
    pain_catastrophizing_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    pain_catastrophizing_questionnaire_pcs6_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 211-218 tbd)


class RcapFearAvoidanceBeliefsQuestionnaire(RcapTable):
    """The Rcap Fear Avoidance Beliefs Questionnaire v03 (FABQ) Instrument."""
    fearavoidance_beliefs_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    fearavoidance_beliefs_questionnaire_v03_fabq_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 220-224 tbd)


class RcapPainResilienceScale(RcapTable):
    """The Rcap Pain Resilience Scale (PRS) Instrument."""
    pain_resilience_scale_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    pain_resilience_scale_prs_complete = Column(Integer,
                                                ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 226-243 tbd)


class RcapPromisSFEmotionalSupport(RcapTable):
    """The Rcap Promis SF v20 Emotional Support 6a Instrument."""
    promis_sf_emotional_support_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    promis_sf_v20_emotional_support_6a_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 245-251 tbd)


class RcapPromisSFInformationalSupport(RcapTable):
    """The Rcap Promis SF v20 Informational Support 6a Instrument."""
    promis_sf_informational_support_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    promis_sf_v20_informational_support_6a_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 253-259 tbd)


class RcapMultidimentionalInventoryOfSubjectiveCognitive(RcapTable):
    """The Rcap Multidimentional Inventory of Subjective Cognitive Instrument."""
    multidimentional_inventory_of_subjective_cognitive_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    multidimentional_inventory_of_subjective_cognitive_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 261-271 tbd)


class RcapAdverseChildhoodExperienceQuestionnaire(RcapTable):
    """The Rcap Adverse Childhood Experience Questionnaire (ACE) Instrument."""
    adverse_childhood_experience_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    adverse_childhood_experience_questionnaire_ace_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 273-285)


class RcapTaps1(RcapTable):
    """The Rcap Taps1 Instrument."""
    taps1_id = Constants.SERIAL_PRIMARY_KEY_COLUMN

    taps1_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 287-292 tbd)


class RcapTaps2(RcapTable):
    """The Rcap Taps1 Instrument."""
    taps2_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    taps2_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 294-341)


class RcapOpiodUseBaseline(RcapTable):
    """The Rcap Opiod Use Baseline v10 Opiod Use i Instrument."""
    opioid_use_baseline_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    opioid_use_baseline_v10_opioid_use_i_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 343-396 tbd)


class RcapOpiodUseAcuteFollowup(RcapTable):
    """The Rcap Opiod Use Acute Followup v10 Opiod Use ii Instrument."""
    opioid_use_acute_followup_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    # Check Rcap to see id the "baseline" portion of the fieldname below has been corrected.
    opioid_use_baseline_v10_opioid_use_ii_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 398-448 tbd)


class RcapOpiodUseLongtermFollowup(RcapTable):
    """The Rcap Opiod Use Longterm Followup v10 Opiod Use iii Instrument."""
    opioid_use_longterm_followup_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    opioid_use_longterm_followup_v10_opioid_use_iii_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 450-500 tbd)


class RcapOpiodSideEffectsAndLikeability(RcapTable):
    """The Rcap Opiod Side Effects and Likeability v03 Instrument."""
    opioid_side_effects_and_likeability_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    opioid_side_effects_and_likeability_v03_side_effec_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 502-523 tbd)


class RcapOpiodAndPainControlSatisfaction(RcapTable):
    """The Rcap Opiod and Pain Control Satisfaction v02 Instrument."""
    opioid_and_pain_control_satisfaction_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    opioid_and_pain_control_satisfaction_v02_satisfact_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 525-527 tbd)


class RcapCurrentOpiodMisuse(RcapTable):
    """The Rcap Current Opiod Misuse v02 Instrument."""
    current_opioid_misuse_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    current_opioid_misuse_v02_comm_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 529-540 tbd)


class RcapRapidAssessmentOfPhysicalActivity(RcapTable):
    """The Rcap Rapid Assessment of Physical Activity (RAPA) v10 Instrument."""
    rapid_assessment_of_physical_activity_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    rapid_assessment_of_physical_activity_v10_rapa_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 542-554)]


class RcapGeneralSensorySensitivity(RcapTable):
    """The Rcap General Sensory Sensitivity v02 GSS8 Instrument."""
    general_sensory_sensitivity_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    general_sensory_sensitivity_v02_gss8_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 556-567 tbd)


class RcapTheBigFiveInventory(RcapTable):
    """The Rcap Big Five Inventory (BFI2S) Instrument."""
    the_big_five_inventory_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    the_big_five_inventory_bfi2s_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 569-599 tbd)


class RcapPatientDemographicsFullPart2(RcapTable):
    """The Rcap Patient Demographics Full Part 2 v03 Instrument."""
    patient_demographics_full_part_2_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    patient_demographics_full_part_2_v03_demographics_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 601-616 tbd)


class RcapSelfadministeredComorbidityQuestionnaire(RcapTable):
    """The Rcap Self-administered Comorbidity Questionnaire (SCQ) v4 Instrument."""
    selfadministered_comorbidity_questionnaire_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    selfadministered_comorbidity_questionnaire_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 618-661 tbd)


class RcapExpectationItems(RcapTable):
    """The Rcap Expectation Items v12 Instrument."""
    expectation_items_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    expectation_items_v12_complete = Column(Integer,
                                            ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 663-665 tbd)


class RcapAcutePhaseTrajectoryItems(RcapTable):
    """The Rcap Acute Phase Trajectory Items v05 Instrument."""
    acute_phase_trajectory_items_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    acute_phase_trajectory_items_v05_acute_daily_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 667-684 tbd)


class RcapDailyItems6Mo(RcapTable):
    """The Rcap Daily Items 6 Month v03 Instrument."""
    daily_items_6_mo_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    daily_items_6_mo_v03_6month_daily_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 686-698 tbd)


class RcapMonth12Followup(RcapTable):
    """The Rcap Month 12 Remote Followup v20 Instrument."""
    month12_followup = Constants.SERIAL_PRIMARY_KEY_COLUMN
    month_remote_followup_v20_12month_followup_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 700-713 tbd)


class RcapFunctionalTesting(RcapTable):
    """The Rcap Functional Testing Instrument."""
    functional_testing_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    functional_testing_complete = Column(Integer,
                                         ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 715-754 tbd)


class RcapQstMcc1(RcapTable):
    """The Rcap QST MCC1 v03 Instrument."""
    qst_mcc1_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    qst_mcc1_v03_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 756-837 tbd)


class RcapCurrentMedications(RcapTable):
    """The Rcap Current Medications v02 Instrument."""
    current_medications_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    current_medications_v02_complete = Column(Integer,
                                              ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 839-843 tbd)


class RcapBloodSampleCRF(RcapTable):
    """The RedCap Blood Sample CRF (bcsp) instrument."""
    rcap_blood_sample_crf_id = Constants.SERIAL_PRIMARY_KEY_COLUMN

    bscp_hrs_since_water = Column(Integer, nullable=True)
    bscp_hrs_since_food = Column(Integer, nullable=True)
    bscp_hrs_since_cafstim = Column(Integer, nullable=True)
    # Rcap-defined (848)integer selector 1-3
    bscp_caff_cups_amt = Column(Integer, nullable=True)
    # Rcap-defined (849) 0-1 binary selector
    bscp_any_vacc = Column(Boolean, nullable=True)
    # Rcap-defined (850) 0-1 binary selector
    bscp_verify_pt = Column(Boolean, nullable=True)
    bscp_ra_initials = Column(String, nullable=True)
    bscp_phleb_by_init = Column(String, nullable=True)
    bscp_sample_obtained = Column(Boolean, nullable=True)
    # Rcap-defined (854)integer selector 1-5
    bscp_no_sample_reason = Column(Integer, nullable=True)
    bscp_samplekit_brcd = Column(String, nullable=True)
    # Should use as biosample creation timestamp if not NULL AND timestamp < current
    bscp_time_blood_draw = Column(CreatedTimeStamp, nullable=True)
    bscp_dt1 = Column(String, nullable=True)
    bscp_lav1_not_obt = Column(Boolean, nullable=True)
    bscp_lav1_brcd = Column(String, nullable=True)
    bscp_paxg_not_obt = Column(Boolean, nullable=True)
    bscp_paxg_brcd = Column(String, nullable=True)
    bscp_dt2 = Column(String, nullable=True)
    bscp_time_centrifuge = Column(Date, nullable=True)
    bscp_lav1_centrif_brcd = Column(String, nullable=True)
    bscp_plugcap_centrif_brcd = Column(String, nullable=True)
    bscp_deg_of_hemolysis = Column(Numeric, nullable=True)
    bscp_dt_3 = Column(String, nullable=True)
    bscp_aliquot_box_brcd = Column(String, nullable=True)
    bscp_buffycoat_na = Column(Boolean, nullable=True)
    bscp_buffycoat_brcd = Column(String, nullable=True)
    bscp_plasma_brcd = Column(String, nullable=True)
    bscp_aliq_cnt = Column(Integer, nullable=True)
    bscp_paxg_box_brcd = Column(String, nullable=True)
    bscp_paxg_aliq_na = Column(Boolean, nullable=True)
    bscp_paxg_aliq_brcd = Column(String, nullable=True)
    bscp_aliquot_freezer_time = Column(Date, nullable=True)
    bscp_dt_4 = Column(String, nullable=True)
    bscp_protocol_dev = Column(Boolean, nullable=True)
    # Rcap-defined (879)integer selector 1-3
    bscp_protocol_dev_reason = Column(Integer, nullable=True)
    bscp_comments = Column(String, nullable=True)
    bscp_procby_initials = Column(String, nullable=True)
    # Rcap-defined (882)integer selector 0-2
    blood_sample_collection_and_processing_crf_complete = Column(Integer,
                                                                 nullable=True)


class RcapImagingItems(RcapTable):
    """The RedCap Imaging Items v11 Instrument."""
    imaging_items_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    imaging_items_v11_complete = Column(Integer,
                                        ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 883-890 tbd)


class RcapImagingMCC1(RcapTable):
    """The RedCap Imaging MCC1 v09 Instrument."""
    imaging_mcc1_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    imaging_mcc1_v09_complete = Column(Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 891-949 tbd)


class RcapStudyVisitFeedback(RcapTable):
    """The RedCap Study Visit Feedback v03 Instrument."""
    study_visit_feedback_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    study_visit_feedback_v03_complete = Column(Integer,
                                               ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 951-985 tbd)


class RcapPatientEncounters(RcapTable):
    """The RedCap Patient Encounters Instrument."""
    patient_encounters_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    patient_encounters_complete = Column(Integer,
                                         ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 987-990 tbd)


class RcapReportableEventDeviation(RcapTable):
    """The RedCap Reportable Event Deviation v03 Instrument."""
    reportable_eventdeviation_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    reportable_eventdeviation_v03_complete = Column(
        Integer, ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 992-1043 tbd)


class RcapEarlyWithdrawal(RcapTable):
    """The RedCap Early Withdrawal v04 Instrument."""
    early_withdrawal_id = Constants.SERIAL_PRIMARY_KEY_COLUMN
    early_withdrawal_v04_complete = Column(Integer,
                                           ForeignKey("status.status_id"))
    # Include other fields? (Rcap fields 1045-1051 tbd)
