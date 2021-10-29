def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    t.get_tokens()
    v = VBR(tapis_client=t)

    if len(args['table_name']) == 0:
        ordered_tables = tableclasses.table_definitions()
    else:
        ordered_tables = [{'table_name': t} for t in args['table_name']]
    ordered_data = data_loads(ordered_tables)

    for od in ordered_data:
        try:
            v.create_row(od)
        except Exception as exc:
            print(exc)


if __name__ == '__main__':

    import argparse
    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis

    from .cli import get_parser
    from .data import data_loads

    parser = get_parser()
    parser.add_argument('table_name',
                        nargs='*',
                        help='Optional: Table name(s)')
    args = parser.parse_args()

    main(vars(args))
