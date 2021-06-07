"""Helper functions for PgREST
"""
import arrow

def camel_to_snake_case(str):
    return ''.join(['_' + i.lower() if i.isupper() else i
                    for i in str]).lstrip('_')


def camel_to_kebab_case(str):
    return ''.join(['-' + i.lower() if i.isupper() else i
                    for i in str]).lstrip('-')


class class_or_instancemethod(classmethod):
    def __get__(self, instance, type_):
        descr_get = super(
        ).__get__ if instance is None else self.__func__.__get__
        return descr_get(instance, type_)

def datetime_to_isodate(date_obj):
    """Convert a Python datetime object to ISO-8601

    Example Response: 2021-06-07T18:42:28.062Z
    """
    d = arrow.get(date_obj).format('YYYY-MM-DDTHH:mm:ss.SSS') + 'Z'
    return d
