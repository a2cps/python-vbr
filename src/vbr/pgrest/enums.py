__all__ = ["Enumeration"]


class Enumeration(object):
    """PgRest enums property"""

    def __init__(self, *args, sorted=False):
        self.values = []
        for a in args:
            if isinstance(a, str):
                self.values.append(a)
            else:
                raise ValueError("Enumeration values can only be strings")
        if sorted:
            self.values.sort()

    def property(self):
        return self.values
