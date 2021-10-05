def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    v = VBR(tapis_client=t)

    if len(args['table_id']) > 0:
        to_drop = args['table_id']
    else:
        to_drop = [t['table_id'] for t in v.list_tables()]

    for t in to_drop:
        print('Deleting {0}'.format(t))
        v.delete_table(t)


if __name__ == '__main__':

    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis

    from .cli import get_parser
    from .data import data_loads

    parser = get_parser()
    parser.add_argument('table_id', nargs='*', help='Optional: Table ID(s)')
    args = parser.parse_args()

    main(vars(args))
