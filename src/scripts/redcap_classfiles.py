def choices_to_dict(choices_str: str) -> dict:
# Utility adapted/extended from code written by M. Vaughn at TACC to parse a REDCap metadata dictionary to generate table schemas and python framework within a database 
# for storing REDCap instrument data. The original code supported a subset of REDCap "field types" and did not utilize other fields present in the REDCap data definitions to
# to specify datatypes (such as integer, numeric, datetime formats), required fields, or valid range. Extensions to this code are intended to leverage this information
# when present in the data dictionary. "Required" and text validation ranges are not enforced by REDCap so will be captured as information but not used to define the table schema.
# This code also supports creating a single set of table schemas from a merged set of REDCap projects with variables added to filter
# tables by project, organization, and other useful criteria. This code is currently under development. 
#
# REDCap data are all exported as strings that require parsing and datatype reclassification to be useful. REDCap "field_types" are as follows: 
#   "text" and "notes" are stored as strings
#   "descriptive" does not directly associate to a data entry and can generally be ignored
#   "yesno" and "truefalse" are boolean, but may need to be typed as string if data is not consistent
#   "radio" is a single answer formatted as an integer (raw data ennumeration), comma separator, and label. Raw data exports will only contain the integer associated with the answer.  
#   "dropdown" is a single answer formatted as an integer (raw data ennumeration), comma separator, and label. Raw data exports will only contain the integer associated with the answer.
#   "checkbox" can be multiple answers expressed as pipe-delimited sets of comma-delimited values. REDCap data can be exported/stored in this format 
#       or as separate variables containing a triple underscore and enumeration (for example, "___1"). Storing multiselect answers as separate variables has generally
#       been the preferred approach for supporting data analysis.
#   "calc" is a formula used to auto-calculate answers based on other fields within the REDCap project. The exported answers could be almost any datatype based on the logic. 
#   "slider" provides a single answer (integer) on a scale of a defined range and slider position. A common range used is 0-100.
#   "file" can be stored as a string or URL
#
# The original code only handles a single checkbox selection. If field_type = "checkbox" AND choices contain a pipe separator indicating multiple checkboxes are present,
# create a separate variable for each choice as "[field_name]___[choice integer]". An example of multi-select checkboxes is early_withdrawal_v04.ewdisreasons.
#
# Used to populate dropdown, checkbox, or slider type
# Generated classes are camelcase; tables are snakecase.
#
# Example: 1, Yes | 0, No
# Example: 0, 0 | .25, 0.25 | .5, 0.5 | 1, 1 | 2, 2 | 4, 4 | 8, 8
# Example: 1, Clinic | 2, Hospital | 3, Specialist
#
# The FOR loop below splits each string containing raw and labeled data into separate answers and strips the pipe and comma separators. 
cdict = {}
for i in choices_str.split("|"):
    i = i.strip()
    ii = i.split(",")
    if len(ii) > 1:
        k = ii[0].strip()
        v = ii[1].strip()
        cdict[k] = v
return cdict

# Testing choices to determine if it is an integer is more straightforward than checking for "integer" in text_validation.
def choices_are_integer(choices_str: str) -> bool:
    cdict = choices_to_dict(choices_str)
    for k, _ in cdict.items():
        try:
            res = int(k)
        except ValueError:
            return False
    return True

# Testing choices to determine if it is a numeric is more straightforward than checking for "number" in text_validation.
def choices_are_numeric(choices_str: str) -> bool:
    cdict = choices_to_dict(choices_str)
    for k, _ in cdict.items():
        try:
            res = float(k)
        except ValueError:
            return False
    return True

# This case should cover truefalse field_type
def choices_are_boolean(choices_str: str) -> bool:
    cdict = choices_to_dict(choices_str)
    values = []
    for k, _ in cdict.items():
        try:
            res = int(k)
            values.append(res)
        except ValueError:
            return False
    if len(values) > 2 or len(values) < 1:
        return False
    for v in values:
        if v not in [0, 1]:
            return False
    return True

# Have we tested this? Both yesno and truefalse REDCap field types are supposed to rendor "1" or "0" as answers.
def choices_are_yesno(choices_str: str) -> bool:
    cdict = choices_to_dict(choices_str)
    values = []
    for k, _ in cdict.items():
        values.append(k)
    if len(values) != 2:
        return False
    for v in values:
        if v not in ["Y", "N"]:
            return False
    return True

# Added truefalse field handling just in case it is NOT handled by the boolean case above.
def choices_are_truefalse(choices_str: str) -> bool:
    cdict = choices_to_dict(choices_str)
    values = []
    for k, _ in cdict.items():
        values.append(k)
    if len(values) != 2:
        return False
    for v in values:
        if v not in ["1", "0"]:
            return False
    return True

def process_data_dict(filename: str, current: dict = None) -> dict:
    """Convert a REDcap Data Dictionary into a minimally processed, actionable Python dict"""
    # {form_name: { field_name: {}}}
    if current is None:
        ddict = {}
    else:
        ddict = current

# Expand the code below to capture: text_validation, text_validation_min, and text_vaidation_max. These entries, when used, 
# can translate directly into datatypes and ranges for the data schema. "Required" is not generally enforced so less useful for schema definition.  
        
    with open(filename, "r") as csvfile:
        ddreader = csv.reader(csvfile)
        # Strip header
        headers = next(ddreader, None)
        for row in ddreader:
            # Form Name
            form_name = row[1]
            # Variable / Field Name
            var_field_name = row[0]
            # Field Type
            field_type = row[3]
            # Field Label
            field_label = row[4]
            # Choices
            choices = row[5]
            # Text Validation (integer, number, date_mdy, date_ymd, date_dmy, datetime_mdy, datetime_ymd, datetime_dmy, datetime_seconds_mdy, datetime_seconds_ymd, datetime_seconds_dmy, time, email, phone, signature)
            text_validation = row[7]
            # Text Validation Min
            text_validation_min = row[8]
            # Text Validation Max
            text_validation_max = row[9]
            # Identifier
            identifier = row[10]
            if identifier == "y":
                identifier = True
            else:
                identifier = False
                           
            if form_name != "" and var_field_name != "":
                if (
                    field_type in SUPPORTED_STRING_TYPES
                    or field_type in SUPPORTED_FREETEXT_TYPES
                ):
                    # print('{0}.{1}'.format(form_name, var_field_name))
                    ddict_entry = {
                        "field_type": field_type,
                        "field_label": field_label,
                        "choices": choices,
                        "identifier": identifier,
                        "source": os.path.basename(filename),
                    }
                    if form_name not in ddict:
                        ddict[form_name] = {}
                    ddict[form_name][var_field_name] = ddict_entry

        return ddict


def build(args):
    logging.info("Building REDcap tableclass files...")

    DEST_DIR = os.path.join(os.path.dirname(redcap.__file__), "autogenerated")
    TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

    # Ensure class files destination exists
    Path(DEST_DIR).mkdir(parents=True, exist_ok=True)

    ddict = {}
    for dd in redcap_data_dictionaries():
        ddict = process_data_dict(filename=dd, current=ddict)

    init_dict = {}
    for form_name, form_config in ddict.items():

        # Set up class def skeleton
        submodule_name = form_name
        # acute_phase_trajectory_items_v01_6month_daily => RcapAcutePhaseTrajectoryItemsV016MonthDaily
        class_name = "Rcap" + snake_to_camel_case(form_name)
        # acute_phase_trajectory_items_v01_6month_daily => Acute Phase Trajectory Items V01 6Month Daily
        class_docstring = snake_to_title_string(form_name)
        autogen_string = "Autogenerated {0} by {1}".format(
            datetime.today().isoformat(), os.path.basename(__file__)
        )
        keyvals = {
            "redcap_form_name": form_name,
            "class_name": class_name,
            "docstring": class_docstring,
            "module_docstring": autogen_string,
            "parent_class_name": "RcapTable",
        }

        # Extend class def with column entries
        keyvals["columns"] = {}
        for col_name, col_config in form_config.items():
            if col_config.get("field_type", None) in SUPPORTED_STRING_TYPES:
                col_type = "String"
            elif col_config.get("field_type", None) in SUPPORTED_FREETEXT_TYPES:
                col_type = "FreeText"

            #####################
            # Translation rules #
            #####################

            # Columns are nullable (until required data is enforced via the REDCap data source)
            col_nullable = "True"

            # Empty default comment
            col_comments = []

            # Type shifts
            if col_name == "guid":
                col_type = "GUID"
            if col_config.get("field_type", None) == "yesno":
                col_type = "Boolean"
            if col_config.get("field_type", None) == "truefalse":
                col_type = "Boolean"


            # Process 'Choices' field
            col_choices = col_config.get("choices", "")
            # Try to override type to be more descriptive of field value based on choices available in REDcap form
            if col_choices != "":
                # TODO Implement casting/handling of string, numeric values to 1/0
                if choices_are_boolean(col_choices) or choices_are_yesno(col_choices):
                    col_type = "Boolean"
                elif choices_are_integer(col_choices):
                    col_type = "Integer"
                elif choices_are_numeric(col_choices):
                    col_type = "Numeric"

            # Property source code comments
            col_label = col_config.get("field_label", "")

            # Handle empty field name
            if col_label == "":
                col_label = "Field Name was empty in Data Dictionary"

            # Ignore multiline field names
            if len(col_label.splitlines()) > 1:
                col_label = "Ignored multiline Field Name in Data Dictionary"

            # Strip leading numeric
            col_label = re.sub("^[0-9]+\.", "", col_label)

            # Strip leading/trailing whitespace
            col_label = col_label.strip()

            # Strip HTML tags
            if col_label.startswith("<"):
                # col_label = 'Ignored HTML Field Name'
                col_label = re.sub("<[^<]+?>", "", col_label)

            # Strip trailing : character
            if col_label.endswith(":"):
                col_label = re.sub(":$", "", col_label)

            # Truncate label to 64 chars
            if len(col_label) > 64:
                col_label = col_label[:61] + "..."

            # Strip trailing whitespace
            col_label = col_label.rstrip("\n")

            # Comments list is turned into source code comments in classfile
            col_comments.append(col_label)
            col_comments.append("Field Type: {0}".format(col_config.get("field_type")))
            if len(col_choices) <= 1:
                col_choices = "N/A"
            col_comments.append("Choices: {0}".format(col_choices))

            # Template rendering data
            keyvals["columns"][col_name] = {
                "comments": col_comments,
                "docstring": col_label,
                "nullable": col_nullable,
                "type": col_type,
            }

# The following REDCap common fields should be added to each REDCap instrument table within the VBR: persistent_id (subject guid), project_id (REDCap project_id "pid"), 
# organization_id (REDCap "dag"), protocol_id (maps to REDCap event_name), creation_time, last_updated_ts, language 
# These were once included in class RcapTable but may have been refactored or omitted. Should these common variables now be added via the Jinja template or somewhere else? 
            
        # Render and write the class file from Jinja template
        with open(os.path.join(TEMPLATES_DIR, CLASS_TEMPLATE)) as tf:
            template = Template(tf.read())
        output = template.render(**keyvals)

        with open(os.path.join(DEST_DIR, submodule_name + ".py"), "w") as cf:
            cf.write(output)
            cf.close()

        # Supports writing 'from <submodule> import <classname> in __init__.py
        init_dict[submodule_name] = class_name

    # Render and write the class file from Jinja template
    with open(os.path.join(TEMPLATES_DIR, INIT_TEMPLATE)) as tf:
        template = Template(tf.read())
    imports = {"imports": init_dict}
    output = template.render(imports)

    with open(os.path.join(DEST_DIR, "__init__.py"), "w") as cf:
        cf.write(output)
        cf.close()

    logging.info("Done")


def clean(args):

    logging.info("Cleaning REDcap tableclass files...")
    DEST_DIR = os.path.join(os.path.dirname(redcap.__file__), "autogenerated")
    TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
    # Ensure class files destination exists
    Path(DEST_DIR).mkdir(parents=True, exist_ok=True)

    # Delete any *.py files in DEST_DIR
    for pyfile in glob.glob(DEST_DIR + "/*.py"):
        os.unlink(pyfile)

    # Write empty __init__.py
    with open(os.path.join(TEMPLATES_DIR, INIT_TEMPLATE)) as tf:
        template = Template(tf.read())
    imports = {
        "module_docstring": "Intentionally empty as class files have not been generated",
        "imports": {},
    }
    output = template.render(imports)
    with open(os.path.join(DEST_DIR, "__init__.py"), "w") as cf:
        cf.write(output)
        cf.close()

    logging.info("Done")


def main(args):
    if args["cmd"] == "build":
        build(args)
    elif args["cmd"] == "clean":
        clean(args)


if __name__ == "__main__":

    import argparse
    import collections
    import csv
    import glob
    import logging
    import os
    import re
    from datetime import datetime
    from pathlib import Path

    import simplejson as json
    from jinja2 import Template

    from vbr.pgrest.utils import snake_to_camel_case, snake_to_title_string
    from vbr.tableclasses import redcap

    from .cli import get_parser
    from .data import redcap_data_dictionaries

    CLASS_TEMPLATE = "redcap_tableclass.py.j2"
    INIT_TEMPLATE = "redcap_tableclasses_init.py.j2"
    # SUPPORTED_STRING_TYPES = ["text", "radio", "dropdown", "checkbox", "yesno"]
    SUPPORTED_STRING_TYPES = ["text", "radio", "dropdown", "checkbox", "yesno", "truefalse", "slider", "file"]
    SUPPORTED_FREETEXT_TYPES = ["notes"]
    parser = get_parser()
    parser.add_argument(
        "cmd", nargs="?", choices=["build", "clean"], default="build", help="Command"
    )
    args = parser.parse_args()

    main(vars(args))
