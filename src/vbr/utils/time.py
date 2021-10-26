"""Manipulate and deal with dates and times.
"""
import datetime
import pytz

__all__ = ['timestamp', 'utc_time_in_seconds']


def timestamp() -> datetime.datetime:
    """Returns the current UTC-localized datetime
    """
    tz = pytz.timezone('UTC')
    return tz.localize(datetime.datetime.utcnow())


def utc_time_in_seconds() -> str:
    """Return string of UTC time in seconds."""
    return str(int(datetime.datetime.today().timestamp()))
