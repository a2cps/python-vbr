def main(args):
    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    v = VBR(tapis_client=t)

    print(v.list_rows('organization'))


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
