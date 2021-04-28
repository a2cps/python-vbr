from . import record

__all__ = ['LinkageRecord']


class LinkageRecord(record.VBRRecord):
    """Extends VBRRecord to represent tables that express parent:child relations
    """
    # Table names
    PARENT = 'parent'
    CHILD = 'child'
    # Eventually used to enforce how many parents an entitiy can have
    MAX_PARENTS = -1
    MIN_PARENTS = 0

    @classmethod
    def primary_key(cls) -> str:
        return '_'.join([cls.CHILD, 'in', cls.PARENT, 'id'])

    @classmethod
    def parent(cls):
        return cls.PARENT

    @classmethod
    def child(cls):
        return cls.CHILD

    @classmethod
    def parent_key(cls):
        return cls.PARENT + '_id'

    @classmethod
    def child_key(cls):
        return cls.CHILD + '_id'

    @classmethod
    def table_name(cls) -> str:
        """The name of the VBR table mapped by this class
        """
        return cls.child() + '_in_' + cls.parent()

    @classmethod
    def fields(cls):
        return [
            (cls.primary_key(), 'serial', True),
            (cls.parent_key(), 'integer', True),
            (cls.child_key(), 'integer', True),
        ]

    @classmethod
    def max_parents(cls):
        return cls.MAX_PARENTS

    @classmethod
    def min_parents(cls):
        return cls.MIN_PARENTS
