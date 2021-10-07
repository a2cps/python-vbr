def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    v = VBR(tapis_client=t)

    tables = tableclasses.table_definitions()
    for t in tables:
        try:
            if len(args['table_name']
                   ) == 0 or t['table_name'] in args['table_name']:
                print('Creating...' + t['table_name'])
                v.create_table_from_definition(t)
                time.sleep(0.125)
        except Exception as exc:
            print(exc)


if __name__ == '__main__':

    # Imports are done here because importing Tapis invokes a
    # multiprocessing pool to load the specs. This in turn causes
    # a strange race condition "An attempt has been made to
    # start a new process before the current process has finished
    # its bootstrapping phase"

    import json
    import os
    import time
    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis
    from .cli import get_parser

    parser = get_parser()
    parser.add_argument('table_name',
                        nargs='*',
                        help='Optional: Table name(s)')
    args = parser.parse_args()

    main(vars(args))
