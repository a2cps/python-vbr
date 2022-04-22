from .loader import TableData


class CollectionTypeData(TableData):
    DATA = [
        {"collection_type_id": 0, "name": "generic collection"},
        {"collection_type_id": 1, "name": "run list:generic"},
        {"collection_type_id": 2, "name": "run list:exRNA"},
        {"collection_type_id": 3, "name": "run list:genetic variants"},
        {"collection_type_id": 4, "name": "run list:proteomics"},
        {"collection_type_id": 5, "name": "run list:lipodomics"},
        {"collection_type_id": 6, "name": "run list:metabolomics"},
    ]
