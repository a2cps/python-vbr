def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    v = VBR(tapis_client=t)

    tables = tableclasses.table_definitions()
    for t in tables:
        try:
            print('Creating...' + t['table_name'])
            v.create_table_from_definition(t)
            time.sleep(1)
        except Exception as exc:
            print(exc)


if __name__ == '__main__':

    # Imports are done here because importing Tapis invokes a
    # multiprocessing pool to load the specs. This in turn causes
    # a strange race condition "An attempt has been made to
    # start a new process before the current process has finished
    # its bootstrapping phase"

    import argparse
    import json
    import os
    import time
    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis

    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--base-url", help="Tapis API url")
    parser.add_argument("-u", "--username", help="Tapis username")
    parser.add_argument("-p", "--password", help="Tapis password")
    args = parser.parse_args()

    main(vars(args))
