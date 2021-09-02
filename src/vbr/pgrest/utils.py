"""Helper functions for PgREST
"""
import arrow


def camel_to_snake_case(strin):
    return ''.join(['_' + i.lower() if i.isupper() else i
                    for i in strin]).lstrip('_')


def camel_to_kebab_case(strin):
    return ''.join(['-' + i.lower() if i.isupper() else i
                    for i in strin]).lstrip('-')


class class_or_instancemethod(classmethod):
    def __get__(self, instance, type_):
        descr_get = super(
        ).__get__ if instance is None else self.__func__.__get__
        return descr_get(instance, type_)


def datetime_to_isodate(date_obj):
    """Convert a Python datetime object to ISO-8601

    Example Response: 2021-06-07 18:42:28.062Z
    """
    d = arrow.get(date_obj).format('YYYY-MM-DD HH:mm:ss.SSS') + 'Z'
    return d


def datetime_to_date(date_obj):
    """Convert a Python datetime object to ISO-8601 date

    Example Response: 2021-06-07
    """
    d = arrow.get(date_obj).format('YYYY-MM-DD')
    return d


def snake_to_camel_case(strin, include_first_word=True):
    temp = strin.split('_')
    if include_first_word:
        return ''.join(ele.title() for ele in temp)
    else:
        return temp[0] + ''.join(ele.title() for ele in temp[1:])


def snake_to_title_string(strin, include_first_word=True):
    temp = strin.split('_')
    if include_first_word:
        return ' '.join(ele.title() for ele in temp)
    else:
        return temp[0] + ' '.join(ele.title() for ele in temp[1:])
