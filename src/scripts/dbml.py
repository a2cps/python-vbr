"""Generates DBML representation of table defs
"""


def pgrest_to_dbml_type(pgrest_type: str) -> str:
    MAPPING = {'serial': 'int', 'text': 'varchar', 'integer': 'int'}
    return MAPPING.get(pgrest_type, pgrest_type)


def pgrest_definition_to_dbml_struct(defn: dict) -> dict:
    dbml = {
        'name': defn['table_name'],
        'note': "'{0}'".format(defn.get('comments', '')),
        'columns': []
    }
    for column_name, column_attrs in defn.get('columns', {}).items():
        col = {}
        col['column_name'] = column_name
        col['column_settings'] = []
        col['column_type'] = pgrest_to_dbml_type(column_attrs['data_type'])
        # Tranform varchar into varchar(char_len) if char_len provided
        if col['column_type'] == 'varchar':
            if column_attrs.get('char_len', None) is not None:
                col['column_type'] = 'varchar({0})'.format(
                    column_attrs.get('char_len'))
        # Primary key and autoincrement
        if column_attrs.get('primary_key', False):
            col['column_settings'].append('primary key')
            # Infer autoincrement int primary key
            if col['column_type'] == 'int':
                col['column_settings'].append('increment')
        # Not null. We must invert from pgrest null property
        if column_attrs.get('null', False):
            col['column_settings'].append('not null')
        # Unique
        if column_attrs.get('unique', False):
            col['column_settings'].append('unique')
        # Comments
        if column_attrs.get('comments', None) is not None:
            comments = column_attrs.get('comments')
            comments = comments.replace("'", "")
            col['column_settings'].append("note: '{0}'".format(comments))
        # Default
        col_default = column_attrs.get('default', None)
        if col_default is not None:
            if col['column_type'] == 'timestamp':
                if col_default.upper() == 'CREATETIME':
                    col_default = "'now()'"
                if col_default.upper() == 'UPDATETIME':
                    col_default = "'now()'"
            elif col['column_type'].startswith('varchar'):
                col_default = "'{0}'".format(col_default)
            col['column_settings'].append("default: {0}".format(col_default))
        # Relations
        if column_attrs.get('foreign_key', False):
            col['column_settings'].append("ref: > {0}.{1}".format(
                column_attrs.get('reference_table'),
                column_attrs.get('reference_column')))
        dbml['columns'].append(col)
    return dbml


def main(args):
    if args['cmd'] == 'build':
        build(args)
    elif args['cmd'] == 'clean':
        clean(args)


def build(args):

    DEST_DIR = os.getcwd()
    TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')

    tdefs = tableclasses.table_definitions()

    rendered_tables = []
    for t in tdefs:
        if t['table_name'] in ALLOW_LIST:
            table = pgrest_definition_to_dbml_struct(t)
            with open(os.path.join(TEMPLATES_DIR, TABLE_TEMPLATE)) as tf:
                template = Template(tf.read())
                output = template.render(table)
                rendered_tables.append(output)

    with open(os.path.join(TEMPLATES_DIR, DOC_TEMPLATE)) as tf:
        template = Template(tf.read())
        output = template.render(tables=rendered_tables)

    with open(os.path.join(DEST_DIR, 'dbml.txt'), 'w') as cf:
        cf.write(output)
        cf.close()

    # Requires @mwvaughn fork of dbml2dot
    # pip install git+https://github.com/mwvaughn/dbml2dot.git
    if args['dotfile']:
        import pydbml.classes
        from dbml2dot.generators import generate_graph_from_dbml

        with open(os.path.join(DEST_DIR, 'dbml.txt'), 'r') as f:
            input_data = f.read()
        dbml = pydbml.PyDBML(input_data)
        graph = generate_graph_from_dbml(dbml)

        with open(os.path.join(DEST_DIR, 'dbml.dot'), "w") as f:
            f.write(graph.to_string())


def clean(args):
    pass


if __name__ == '__main__':

    import argparse
    import json
    import os
    from jinja2 import Template
    from pathlib import Path

    from vbr import tableclasses
    from vbr.pgrest.utils import snake_to_camel_case, snake_to_title_string
    from .cli import get_parser

    DOC_TEMPLATE = 'dbml_doc.txt.j2'
    TABLE_TEMPLATE = 'dbml_table.txt.j2'
    LINK_TEMPLATE = 'dbml_link.txt.j2'

    ALLOW_LIST = [
        'anatomy', 'biosample', 'contact', 'container', 'container_type',
        'container_in_container', 'data_event', 'location', 'measurement',
        'measurement_type', 'organization', 'project', 'protocol', 'reason',
        'shipment', 'status', 'subject', 'unit', 'container_in_shipment', 
        'data_event_in_subject', 'data_event_in_biosample', 'data_event_in_measurement',
        'data_event_in_shipment', 'measurement_from_measurement',
        'rcap_consented_participant_information', 'blood_sample_collection_and_processing_crf'
    ]

    parser = get_parser()
    parser.add_argument('cmd',
                        nargs='?',
                        choices=['build', 'clean'],
                        default='build',
                        help='Command')
    parser.add_argument('--dotfile',
                        action='store_true',
                        help='Also generate a dotfile output')
    args = parser.parse_args()

    main(vars(args))
