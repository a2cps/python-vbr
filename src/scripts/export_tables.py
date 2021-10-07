def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    v = VBR(tapis_client=t)

    if len(args['table_name']) > 0:
        to_export = args['table_name']
    else:
        to_export = [t['table_name'] for t in v.list_tables()]

    for t in to_export:
        print('Exporting {0}'.format(t))

        output_dir = args.get('output_dir', None)
        if output_dir is None:
            # target is "exports" directory at top level of python-vbr
            output_dir = exports_directory()
        filename = os.path.join(output_dir, '.'.join([t, 'csv']))

        data = [r.dict() for r in v.list_rows(root_url=t, limit=100000)]
        if len(data) > 0:
            keys = data[0].keys()
            with open(filename, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)


if __name__ == '__main__':

    import csv
    import os

    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis

    from .cli import get_parser, exports_directory
    from .data import data_loads

    parser = get_parser()
    parser.add_argument('-O',
                        '--output-dir',
                        dest='output_dir',
                        help='Output directory [$pwd]')
    parser.add_argument('table_name',
                        nargs='*',
                        help='Optional: Table Name(s)')

    args = parser.parse_args()

    main(vars(args))
