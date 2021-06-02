import json

class class_or_instancemethod(classmethod):
    def __get__(self, instance, type_):
        descr_get = super().__get__ if instance is None else self.__func__.__get__
        return descr_get(instance, type_)

class PgRestColumn(object):
    DATA_TYPE = None
    @classmethod
    def properties(cls):
        return {'data_type': cls.DATA_TYPE}

class ForeignKey(object):
    def __init__(self, source, on_delete='cascade', on_update='cascade'):
        self.FK = True
        (self.reference_table, self.reference_column) = source.split('.')
        self.on_delete = on_delete
        self.on_update = on_update

    def properties(self):
        return {'FK': self.FK,
                'reference_table': self.reference_table,
                'reference_column': self.reference_column,
                'on_delete': self.on_delete}

class UniqueConstraint(object):
    pass

# TODO - Support varchar[]
# TODO - Support int[]
# TODO - Support enumerations
# TODO - Better support for DateTime

class Integer(PgRestColumn):
    DATA_TYPE = 'integer'

class Boolean(PgRestColumn):
    DATA_TYPE = 'boolean'

class Text(PgRestColumn):
    DATA_TYPE = 'text'

class String(PgRestColumn):
    DATA_TYPE = 'varchar'
    CHAR_LEN = 255

    def __init__(self, max_size=None):
        self.CHAR_LEN = max_size
    
    @class_or_instancemethod
    def properties(self_or_cls):
        return {'data_type': self_or_cls.DATA_TYPE, 'char_len': self_or_cls.CHAR_LEN}

class DateTime(PgRestColumn):
    DATA_TYPE = 'datetime'

class Serial(PgRestColumn):
    DATA_TYPE = 'serial'

class Column(object):
    """PgREST Column
    """
    def __init__(self,
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
        self.primary_key = primary_key
        self.unique = unique
        self.nullable = nullable
        self.default = default

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
            all_props = {**all_props, **fk_props}        

        return all_props

class Table(object):
    """PgREST Table
    """
    __tablename__ = 'table'
    __rooturl__ = None
    __extra_constraints__ = []

    @class_or_instancemethod
    def table_name(self):
        return self.__tablename__

    @class_or_instancemethod
    def root_url(self):
        if self.__rooturl__ is not None:
            return self.__rooturl__
        else:
            return self.__tablename__

    @class_or_instancemethod
    def columns(self):
        defn = {}
        for aname in dir(self):
            attr = getattr(self, aname)
            if isinstance(attr, Column):
                defn[aname] = attr.property()
        return defn

    @class_or_instancemethod
    def definition(self):
        data = {'table_name': self.table_name(),
                'root_url': self.root_url(),
                'columns': self.columns()
                }
        return data

    @class_or_instancemethod
    def to_json(self):
        return json.dumps(self.definition(), indent=4)

    @class_or_instancemethod
    def __repr__(self):
        return self.to_json()

