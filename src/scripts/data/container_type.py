from .loader import TableData


class ContainerTypeData(TableData):
    DATA = [
        {"container_type_id": 0, "name": "default container (virtual)"},
        {"container_type_id": 1, "name": "generic box"},
        {"container_type_id": 2, "name": "parcel"},
        {"container_type_id": 3, "name": "blood aliquot freezer box"},
        {"container_type_id": 4, "name": "paxgene freezer box"},
        {"container_type_id": 5, "name": "-80C freezer"},
        {"container_type_id": 6, "name": "-20C freezer"},
        {"container_type_id": 7, "name": "4C refrigerator"},
        {"container_type_id": 8, "name": "liquid nitrogen storage"},
        {"container_type_id": 9, "name": "24 well plate"},
        {"container_type_id": 10, "name": "96 well plate"},
        {"container_type_id": 11, "name": "384 well plate"},
    ]
