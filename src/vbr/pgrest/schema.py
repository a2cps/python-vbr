import hashlib
import inspect
import json
import re

from .column import Column
from .config import Config
from .constraints import Constraint
from .enums import Enumeration
from .utils import camel_to_kebab_case, camel_to_snake_case


def _redcap_aware_camel_to_snake_case(class_name: str):
    # NOTE - I hate this. Remember to take it out if we ever reuse this code
    #
    # This is a hack to support the 'partN' strings that arise in Redcap classes"""
    table_name = camel_to_snake_case(class_name)
    # Only attempt this in case of redcap tables
    if table_name.startswith("rcap"):
        return re.sub("(part)([0-9]{1,3})", r"\1_\2", table_name)
    else:
        return table_name


class PgrestSchema(object):
    def __init__(self, parent):
        self.parent = parent

    @property
    def table_name(self):
        if self.parent.__tablename__ is None:
            return _redcap_aware_camel_to_snake_case(self.parent.__class__.__name__)
        else:
            return self.parent.__tablename__

    @property
    def root_url(self):
        if self.parent.__rooturl__ is not None:
            return camel_to_kebab_case(self.parent.__class__.__name__)
        else:
            return self.table_name

    @property
    def columns(self):
        defn = {}
        for k, v in self.parent.__class_attrs__.items():
            if isinstance(v, Column):
                defn[k] = v.property()
        return defn

    @property
    def column_names(self):
        defn = []
        for k, v in self.parent.__class_attrs__.items():
            if isinstance(v, Column):
                defn.append(k)
        defn.sort()
        return defn

    @property
    def enumerations(self):
        defn = {}
        for k, v in self.parent.__class_attrs__.items():
            if isinstance(v, Enumeration):
                defn[k] = v.property()
        return defn

    @property
    def constraints(self):
        defn = {}
        for k, v in self.parent.__class_attrs__.items():
            if isinstance(v, Constraint):
                ctype = v.constraint_type()
                cvalues = v.property()
                if ctype not in defn:
                    defn[ctype] = {}
                # hash table name
                table_name = hashlib.md5(self.table_name.encode("utf-8")).hexdigest()[
                    :7
                ]
                key = "{0}_{1}".format(k, table_name)
                defn[ctype][key] = cvalues
        return defn

    @property
    def definition(self):
        data = {
            "table_name": self.table_name,
            "root_url": self.root_url,
            "columns": self.columns,
        }

        # Extend table definition with enums if provided
        enums = self.enumerations
        if enums != {}:
            data["enums"] = enums

        # Feature gate: Support table-level constraints
        # https://github.com/tapis-project/paas/issues/12
        constraints = self.constraints
        if Config.TABLE_CONSTRAINTS:
            if constraints != {}:
                data["constraints"] = constraints

        # Feature gate: Support for table comment property
        # https://github.com/tapis-project/paas/issues/11
        if Config.TABLE_COMMENTS:
            if self.comment is not None and self.comment != "":
                data["comments"] = self.comment

        return data

    @property
    def comment(self):
        return inspect.getdoc(self.parent).strip()

    def to_json(self):
        return json.dumps(self.definition, indent=4, sort_keys=True)
