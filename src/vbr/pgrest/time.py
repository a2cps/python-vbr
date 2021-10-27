"""Manipulate and deal with dates and times.
"""
import datetime

__all__ = ['timestamp']


def timestamp():
    """Return UTC timestamp formatted for pgrest.
    """
    DEST = '%Y-%m-%dT%H:%M:%S.%fZ'
    return datetime.datetime.utcnow().strftime(DEST)
