import inspect
import json

from .column import Column
from .constraints import Constraint
from .enums import Enumeration
from .utils import camel_to_kebab_case, camel_to_snake_case


class PgrestSchema(object):
    def __init__(self, parent):
        self.parent = parent

    @property
    def table_name(self):
        if self.parent.__tablename__ is None:
            return camel_to_snake_case(self.parent.__class__.__name__)
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
                defn[ctype][k] = cvalues
        return defn

    @property
    def definition(self):
        data = {
            'table_name': self.table_name,
            'root_url': self.root_url,
            'columns': self.columns
        }

        # Extend table definition with enums if provided
        enums = self.enumerations
        if enums != {}:
            data['enums'] = enums

        # TODO - support constraints once pgrest does
        constraints = self.constraints
        if constraints != {}:
            data['constraints'] = constraints

        # TODO - support for requested comment property
        if self.comment is not None and self.comment != '':
            data['comment'] = self.comment

        return data

    @property
    def comment(self):
        return inspect.getdoc(self.parent)

    def to_json(self):
        return json.dumps(self.definition, indent=4, sort_keys=True)
