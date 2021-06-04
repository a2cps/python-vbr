from typing import Any
from attrdict import AttrDict
import json
import inspect


def camel_to_snake_case(str):
    return ''.join(['_' + i.lower() if i.isupper() else i
                    for i in str]).lstrip('_')


class class_or_instancemethod(classmethod):
    def __get__(self, instance, type_):
        descr_get = super(
        ).__get__ if instance is None else self.__func__.__get__
        return descr_get(instance, type_)


class DependencySolver(object):
    def __init__(self, definitions):

        # Lists of table definitions
        self.to_do = definitions
        self.deferred = []
        # List of table names
        self.completed = []
        # Unresolved dependencies
        self.dependencies = []

    def ordered_emit(self):

        ordered = []
        max_iterations = len(self.to_do) * 2
        iterations = 0

        while self.to_do and (iterations <= max_iterations):

            # find dependencies
            tdef = self.to_do.pop()
            tdef_table_name = tdef['table_name']
            print(tdef_table_name)
            tdef_cols = tdef['columns']

            # Are any foreign keys defined? If so, do they
            # refer to tables that have not been completed. If
            # so, put the definition back on the queue
            dep_found = False
            for k, v in tdef_cols.items():
                if v.get('FK', False):
                    if v['reference_table'] not in self.completed:
                        print('dependency: ' + v['reference_table'])
                        dep_found = True
                        break

            if not dep_found:
                self.completed.append(tdef_table_name)
                ordered.append(tdef)
            else:
                print('Queueing ' + tdef_table_name)
                # self.to_do.append(tdef)
                self.to_do.insert(0, tdef)
                print(len(self.to_do))

            iterations = iterations + 1

        print([t['table_name'] for t in self.to_do])
        print([t['table_name'] for t in ordered])

        return ordered


# TODO - implement type validation of defaults
# TODO - implement comment keyword argument in constructor
class PgRestColumn(object):
    DATA_TYPE = None
    PYTHON_TYPE = None

    @classmethod
    def properties(cls):
        return {'data_type': cls.DATA_TYPE}

    @classmethod
    def validate(cls, value):

        if value is None:
            return True

        if cls.PYTHON_TYPE is None:
            return True
        else:
            return isinstance(value, cls.PYTHON_TYPE)


class ForeignKey(object):
    def __init__(self, source, on_delete='cascade', on_update='cascade'):
        self.FK = True
        (self.reference_table, self.reference_column) = source.split('.')
        self.on_delete = on_delete
        self.on_update = on_update

    def properties(self):
        return {
            'FK': self.FK,
            'reference_table': self.reference_table,
            'reference_column': self.reference_column,
            'on_delete': self.on_delete
        }


class Constraint(object):
    def __init__(self, *args, **kwargs):
        pass


class UniqueConstraint(Constraint):
    def __init__(self, *args, **kwargs):
        pass


class Enumeration(object):
    """PgRest enums property
    """
    def __init__(self, *args, sorted=False):
        self.values = []
        for a in args:
            if isinstance(a, str):
                self.values.append(a)
            else:
                raise ValueError('Enumeration values can only be strings')
        if sorted:
            self.values.sort()

    def property(self):
        return self.values


# TODO - Better support for DateTime


class Integer(PgRestColumn):
    DATA_TYPE = 'integer'
    PYTHON_TYPE = int


class Boolean(PgRestColumn):
    DATA_TYPE = 'boolean'
    PYTHON_TYPE = bool


class Text(PgRestColumn):
    DATA_TYPE = 'text'
    PYTHON_TYPE = str


class String(PgRestColumn):
    DATA_TYPE = 'varchar'
    PYTHON_TYPE = str
    CHAR_LEN = 255

    def __init__(self, max_size=None):
        self.CHAR_LEN = max_size

    @class_or_instancemethod
    def properties(self_or_cls):
        return {
            'data_type': self_or_cls.DATA_TYPE,
            'char_len': self_or_cls.CHAR_LEN
        }


class DateTime(PgRestColumn):
    DATA_TYPE = 'datetime'


class Serial(PgRestColumn):
    DATA_TYPE = 'serial'
    PYTHON_TYPE = int


class StringList(PgRestColumn):
    DATA_TYPE = 'varchar[]'
    PYTHON_TYPE = None


class IntList(PgRestColumn):
    DATA_TYPE = 'int[]'
    PYTHON_TYPE = None


class Column(object):
    """PgREST Column
    """
    def __init__(
            self,
    #  cname,
            ctype,
            *args,
            primary_key=False,
            unique=False,
            nullable=False,
            default=None,
            **kwargs):

        # self.cname = cname
        self.ctype = ctype
        if self.ctype.validate(default):
            self.default = default
        else:
            raise ValueError('Invalid type for default')

        self.primary_key = primary_key
        self.unique = unique
        self.nullable = nullable
        self.relations = []

        self.fk = None
        for a in args:
            if isinstance(a, ForeignKey):
                self.fk = a

    def property(self):
        all_props = self.ctype.properties()
        if self.default is not None:
            all_props['default'] = self.default
        if self.primary_key:
            all_props['primary_key'] = True
        if self.unique:
            all_props['unique'] = True
        all_props['null'] = self.nullable

        if self.fk is not None:
            fk_props = self.fk.properties()
            self.relations.append(fk_props['reference_table'])
            all_props = {**all_props, **fk_props}

        return all_props


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
            return self.parent.__rooturl__
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
                defn[k] = v.property()
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
        return data

    @property
    def comment(self):
        return inspect.getdoc(self.parent)

    def to_json(self):
        return json.dumps(self.definition, indent=4)


class Table(object):
    """PgREST Table
    """
    __tablename__ = None
    __rooturl__ = None

    # TODO - support for generating create/update JSON for PgREST

    def __init__(self, **kwargs):

        self.__class_attrs__ = {}
        self.__schema__ = PgrestSchema(self)

        # Move class-defined attributes into a private var
        # Create regular properties holding values passed in via constructor
        for aname in dir(self):
            attr = getattr(self, aname)
            if isinstance(attr, (Column, Enumeration, Constraint)):
                self.__class_attrs__[aname] = attr
                # TODO - use validate() from attr
                setattr(self, aname, kwargs.get(aname, None))
