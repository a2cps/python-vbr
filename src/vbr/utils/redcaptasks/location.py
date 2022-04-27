__all__ = [
    "redcap_default_ship_to_vbr_location",
    "redcap_shipping_mcc_to_vbr_location",
    "redcap_shipping_mcc_to_vbr_project",
    "redcap_data_access_group_to_vbr_location",
]

MAPPINGS = {
    "mcc_vbr_location": {"1": "11", "2": "12", "3": "13", "4": "20"},
    "mcc_vbr_project": {"1": "2", "2": "2", "3": "2", "4": "3"},
    "dag_vbr_location": {
        "rush_university_me": "11",
        "uchicago": "12",
        "northshore": "13",
        "university_of_mich": "20",
        "spectrum_health": "21",
    },
}


def redcap_default_ship_to_vbr_location() -> str:
    """Returns the VBR Location ID shipment location for UCSD"""
    # Response is a location_id mapped to these locations
    # See src/scripts/data/location.csv
    return "1"


def redcap_shipping_mcc_to_vbr_location(mcc: str) -> str:
    """Return the VBR Location ID for a REDcap shipment info MCC value"""
    # mcc is hard-coded in REDcap. Currently, as follows in
    # https://redcap.tacc.utexas.edu/redcap_v10.6.11/Design/data_dictionary_codebook.php?pid=20
    # 1. Rush 2. University of Chicago 3. Northshore 4. University of Michigan
    #
    # Response is a location_id mapped to these locations
    # See src/scripts/data/location.csv
    return MAPPINGS["mcc_vbr_location"].get(str(mcc), "0")


def redcap_shipping_mcc_to_vbr_project(mcc: str) -> str:
    """Return the VBR Project ID for a REDcap shipment info MCC value"""
    # mcc is hard-coded in REDcap. Currently, as follows in
    # https://redcap.tacc.utexas.edu/redcap_v10.6.11/Design/data_dictionary_codebook.php?pid=20
    # 1. Rush 2. University of Chicago 3. Northshore 4. University of Michigan
    #
    # Response is a project_id mapped to these locations
    # See src/scripts/data/project.py
    return MAPPINGS["mcc_vbr_project"].get(str(mcc), "0")


def redcap_data_access_group_to_vbr_location(data_access_group: str) -> str:
    # Redcap form responses include a data access group. This can be
    # used to infer the location of VBR entities derived from redcap
    # records.
    # Response is a location_id mapped to these locations
    return MAPPINGS["dag_vbr_location"].get(str(data_access_group), "0")
