def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    t.get_tokens()
    v = VBR(tapis_client=t)

    # Default to a list of tables ordered by mutual dependency
    if len(args['table_name']) == 0:
        ordered_tables = [
            t['table_name'] for t in tableclasses.table_definitions()
        ]
    else:
        ordered_tables = args['table_name']

    import_dir = args.get('dumps_dir', None)
    if import_dir is None:
        # target is "exports" directory at top level of python-vbr
        import_dir = exports_directory()

    # Build a list of VBR table objects to add
    records_to_add = []
    for t in ordered_tables:
        print('Loading table {0}'.format(t))
        try:
            # get class definition for the table
            cl = tableclasses.class_from_table(t)
            # print(cl)
            # Read CSV into VBR objects
            with open(os.path.join(import_dir, '{0}.csv'.format(t)),
                      'r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=',')
                for row in csv_reader:
                    vbr_record = cl(**row)
                    records_to_add.append(vbr_record)
        except FileNotFoundError:
            pass

    print(len(records_to_add), ' records to add')

    for od in records_to_add:
        try:
            v.create_row(od)
        except Exception as exc:
            print(exc)


if __name__ == '__main__':

    import argparse
    import csv
    import os

    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis

    from .cli import get_parser, exports_directory
    from .data import data_loads

    parser = get_parser()
    parser.add_argument('-O',
                        '--dumps-dir',
                        dest='dumps_dir',
                        help='Dumps directory [exports]')
    parser.add_argument('table_name',
                        nargs='*',
                        help='Optional: Table name(s)')
    args = parser.parse_args()

    main(vars(args))
