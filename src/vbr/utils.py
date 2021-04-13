import datetime
import pytz
from . import constants


def timestamp() -> datetime.datetime:
    """Returns the current UTC-localized datetime
    """
    tz = pytz.timezone('UTC')
    return tz.localize(datetime.datetime.utcnow())


def timestring_to_timestamp(
    record_time: str,
    source_timezone: str = constants.SOURCE_TIMEZONE,
    destination_timezone: str = constants.DATABASE_TIMEZONE
) -> datetime.datetime:
    """Transform a time string into a localized datetime
    """
    # Parseable timestring formats, in order of preference
    FORMATS = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d']
    dt = None
    for df in FORMATS:
        try:
            dt = datetime.datetime.strptime(record_time, df)
            break
        except ValueError:
            pass

    if dt is None:
        raise ValueError(
            '{0} cannot be converted to a timestamp'.format(record_time))

    tz1 = pytz.timezone(source_timezone)
    tz2 = pytz.timezone(destination_timezone)
    dt = tz1.localize(dt)
    return dt.astimezone(tz2)
