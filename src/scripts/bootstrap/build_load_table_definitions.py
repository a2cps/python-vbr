def main(args):

    t = Tapis(base_url=args['base_url'], username=args['username'], password=args['password'])
    v = VBR(tapis_client=t)
    print([a['table_name'] for a in v.list_tables()])
    # raise SystemError()

    # tables = tableclasses.table_definitions()
    # for t in tables:
    #     try:
    #         v.create_table_from_definition(t)
    #     except Exception as exc:
    #         raise

if __name__ == '__main__':

    # Imports are done here because importing Tapis invokes a 
    # multiprocessing pool to load the specs. This in turn causes
    # a strange race condition "An attempt has been made to 
    # start a new process before the current process has finished 
    # its bootstrapping phase"
    
    import argparse
    import json
    import os
    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis

    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", help="Tapis API url")
    parser.add_argument("--username", help="Tapis username")
    parser.add_argument("--password", help="Tapis password")
    args = parser.parse_args()

    main(vars(args))
