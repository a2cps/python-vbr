import datetime
import os

import pytz

from .constants import REDCAP_SERVER_TIMEZONE

__all__ = ["redcap_to_pgrest_datetime", "redcap_to_datetime"]


def redcap_to_datetime(date_time_str: str, source_timezone: str = None) -> str:
    """Tranform REDcap time strings into datetime"""
    if source_timezone is None:
        source_timezone = "America/Chicago"

    # 2021-04-30 11:53 -> 2021-04-30T11:53:00.00000
    # Source formats
    SOURCES = (
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S",
    )
    timezone_now = pytz.timezone(source_timezone)
    # UTC
    timezone_utc = pytz.timezone("Europe/London")
    for f in SOURCES:
        try:
            dt = datetime.datetime.strptime(date_time_str, f)
            dtl = timezone_now.localize(dt)
            dtutc = dtl.astimezone(timezone_utc)
            return dtutc
        except ValueError:
            pass
    raise ValueError("{0} not in a recognized strptime format".format(date_time_str))


def redcap_to_pgrest_datetime(date_time_str: str, source_timezone: str = None) -> str:
    """Tranform REDcap time strings into ISO-8601 format."""
    # Destination format
    DEST = "%Y-%m-%dT%H:%M:%S.%fZ"
    dtutc = redcap_to_datetime(date_time_str, source_timezone)
    return dtutc.strftime(DEST)
