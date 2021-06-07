__all__ = ['Constraint', 'UniqueConstraint', 'Signature']


class Constraint(object):
    TYPE = None

    def __init__(self, *args, **kwargs):
        pass

    def constraint_type(self):
        return self.TYPE

    def property(self):
        pass


class UniqueConstraint(Constraint):
    TYPE = 'unique'

    def __init__(self, *args, **kwargs):
        self.values = []
        for a in args:
            if isinstance(a, str):
                self.values.append(a)

    def property(self):
        return self.values


class Signature(UniqueConstraint):
    pass
