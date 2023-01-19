import os

import requests

from . import crf
from .constants import *

__all__ = ["record_by_id", "records_by_id"]


def records_by_id(
    record_id: str,
    instrument: str = None,
    event: str = None,
    token: str = None,
    api_url: str = None,
    transform=True,
    fields = None
) -> list:
    """Return REDcap records for a given record, instrument, event."""

    # Query REDCap API with token for message.record.
    # Raise exception on error.
    query = {
        "token": token,
        "content": "record",
        "format": "json",
        "type": "flat",
        "csvDelimiter": "",
        "records[0]": record_id,
        "rawOrLabel": "raw",
        "rawOrLabelHeaders": "raw",
        "exportCheckboxLabel": "false",
        "exportSurveyFields": "false",
        "exportDataAccessGroups": "true",
        "returnFormat": "json",
    }

    if instrument is not None:
        query["forms[0]"] = instrument
    if event is not None:
        query["events[0]"] = event
    if api_url is None:
        api_url = os.environ.get(
            REDCAP_API_ENV_VAR, "https://redcap.tacc.utexas.edu/api/"
        )
    if fields is not None:
        query["fields[0]"] = fields

    r = requests.post(api_url, data=query)
    r.raise_for_status()

    # Unpack from list because we are querying for a single record
    raw_records = r.json()
    return_records = []
    for rec in raw_records:
        # clean any recs with just empty strings for values, 
        # ie, any key that isn't the data access group
        vals = [v for k,v in rec.items() if k not in ['redcap_data_access_group','redcap_event_name','record_id']]
        if set(vals) == {''}:
            # if the values are empty go to the next loop iteration
            continue

        if transform:
            return_records.append(crf.transform_redcap_record(rec))
        else:
            return_records.append(rec)

    return return_records


def record_by_id(
    record_id: str,
    instrument: str = None,
    event: str = None,
    token: str = None,
    api_url: str = None,
    transform=True,
    field = None,
    single_record = True,
) -> dict:
    """Return first REDcap record for a given record, instrument, event."""
    if single_record == True:
        return records_by_id(record_id, instrument, event, token, api_url, transform, field)[0]
    else:
        return records_by_id(record_id, instrument, event, token, api_url, transform, field)
