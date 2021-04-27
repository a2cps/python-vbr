from .. import record

class LinkageRecord(record.VBRRecord):
    PARENT = 'parent'
    CHILD = 'child'

    @classmethod
    def primary_key(cls) -> str:
        return '_'.join([cls.CHILD, 'in', cls.PARENT, 'id'])

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
        return cls.child_key() + '_in_' + cls.parent_key()

    @classmethod
    def fields(cls):
        return [
            (cls.primary_key(), 'serial', True),
            (cls.parent_key(), 'integer', True),
            (cls.child_key(), 'integer', True),
        ]

class BioSampleInDataset(LinkageRecord):
    """VBR biosample_in_dataset
    """
    PARENT = 'dataset'
    CHILD = 'biosample'


class DatasetInDataset(LinkageRecord):
    """VBR dataset_in_dataset
    """
    PARENT = 'dataset'
    CHILD = 'dataset'

    @classmethod
    def parent_key(cls):
        return 'parent_' + cls.PARENT + '_id'

class FileInDataset(LinkageRecord):
    """VBR file_in_dataset
    """
    PARENT = 'dataset'
    CHILD = 'file'
