from .loader import TableData


class MeasurementTypeData(TableData):
    DATA = [
        {
            'measurement_type_id': 1,
            'name': 'generic biological sample'
        },
        {
            'measurement_type_id': 2,
            'name': 'whole blood'
        }, 
        {
            'measurement_type_id': 3,
            'name': 'serum or plasma'
        }, 
        {
            'measurement_type_id': 4,
            'name': 'buffycoat'
        },
        {
            'measurement_type_id': 5,
            'name': 'paxgene rna'
        },
        {
            'measurement_type_id': 6,
            'name': 'paxgene dna'
        }
    ]
