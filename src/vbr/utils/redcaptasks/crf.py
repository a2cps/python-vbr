import re
from .constants import *

__all__ = ['transform_redcap_record']


def transform_redcap_record(record: dict) -> dict:
    """Transform a Redcap record from API response into a dict that can be used to populate a VBR RcapTable.
    """
    # delete keys that we will never store in VBR
    DELETE_KEYS = ['redcap_repeat_instrument', 'redcap_repeat_instance']
    for k in DELETE_KEYS:
        try:
            del record[k]
        except KeyError:
            pass
    # Find checkbox or multi keys and transform into values
    MULTI = re.compile('___([0-9]{1,})$')
    all_keys = list(record.keys())
    selector_keys = {}
    final_selector_keys = {}
    DELETE_MULTI_KEYS = []
    for k in all_keys:
        m = MULTI.search(k)
        if m:
            DELETE_MULTI_KEYS.append(k)
            key_root = k[:m.span()[0]]
            key_multi = m[1]
            if key_root not in selector_keys:
                selector_keys[key_root] = {}
            selector_keys[key_root][key_multi] = record.get(k)
    for k, v in selector_keys.items():
        final_selector_keys[k] = 0
        for i, j in v.items():
            if int(j) == 1:
                final_selector_keys[k] = int(i)
    # Delete original multi keys
    for k in DELETE_MULTI_KEYS:
        try:
            del record[k]
        except KeyError:
            pass
    # Replace them with final_selector_keys
    for k, v in final_selector_keys.items():
        record[k] = v
    return record
