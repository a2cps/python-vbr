from .linkage_record import LinkageRecord


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
