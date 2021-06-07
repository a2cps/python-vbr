__all__ = ['ForeignKey']


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
