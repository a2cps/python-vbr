from .config import Config

__all__ = ['ForeignKey']


class ForeignKey(object):
    def __init__(self, source, on_delete='cascade', on_update='cascade'):
        self.foreign_key = True
        (self.reference_table, self.reference_column) = source.split('.')
        self.on_delete = on_delete
        self.on_update = on_update

    def properties(self):

        # Feature gate: Use more descriptive name 'foreign_key'
        # https://github.com/tapis-project/paas/issues/6
        if Config.COLUMN_USE_FOREIGN_KEY_PROPERTY_NAME:
            fk_prop_name = 'foreign_key'
        else:
            fk_prop_name = 'FK'

        return {
            fk_prop_name: self.foreign_key,
            'reference_table': self.reference_table,
            'reference_column': self.reference_column,
            'on_delete': self.on_delete
        }
