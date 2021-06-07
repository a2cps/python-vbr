from .loader import TableData


class AnatomyData(TableData):
    DATA = [{
        'anatomy_id': 1,
        'name': 'blood',
        'description': 'whole blood',
        'id': 'UBERON:0000178'
    }, {
        'anatomy_id': 2,
        'name': 'blood plasma',
        'description': 'blood plasma',
        'id': 'UBERON:0001969'
    }, {
        'anatomy_id': 3,
        'name': 'urine',
        'description': 'urine sample',
        'id': 'UBERON:0001088 UBERON:0001988 UBERON:0001037 UBERON:0001088'
    }, {
        'anatomy_id': 4,
        'name': 'feces',
        'description': 'fecal sample',
        'id': 'UBERON:0001988'
    }, {
        'anatomy_id': 5,
        'name': 'strand of hair',
        'description': 'hair sample',
        'id': 'UBERON:0001037'
    }, {
        'anatomy_id': 6,
        'name': 'brain',
        'description': 'full brain scan',
        'id': 'UBERON:0000955'
    }]
