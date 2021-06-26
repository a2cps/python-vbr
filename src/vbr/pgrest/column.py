from .config import Config
from .foreign_key import ForeignKey

__all__ = ['Column', 'ForeignKey']


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
    
    @classmethod
    def instantiate(cls, value):
        return value


class Column(object):
    """PgREST Column
    """
    def __init__(
            self,
    #   cname,
            ctype,
            *args,
            primary_key=False,
            unique=False,
            nullable=False,
            default=None,
            comments=None,
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
        self.comments = comments
        self.relations = []

        self.fk = None
        for a in args:
            if isinstance(a, ForeignKey):
                self.fk = a

    def property(self):

        all_props = self.ctype.properties()

        # If default is specified for Column, use that
        # value. Otherwise, if default already was returned
        # from the items properties() method, use that
        # value. If no default at all, don't provide a
        # 'default' value for the column
        if self.default is not None:
            all_props['default'] = self.default

        if self.primary_key:
            all_props['primary_key'] = True
        if self.unique:
            all_props['unique'] = True
        all_props['null'] = self.nullable

        # Feature gate: Support per-column comments
        # https://github.com/tapis-project/paas/issues/10
        if Config.COLUMN_COMMENTS:
            if self.comments is not None:
                all_props['comments'] = self.comments

        if self.fk is not None:
            fk_props = self.fk.properties()
            self.relations.append(fk_props['reference_table'])
            all_props = {**all_props, **fk_props}

        return all_props
