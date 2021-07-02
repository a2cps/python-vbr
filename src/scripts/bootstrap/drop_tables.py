def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    v = VBR(tapis_client=t)
    tables = v.list_tables()
    for t in tables:
        print('Deleting {0}'.format(t['table_id']))
        v.delete_table(t['table_id'])


if __name__ == '__main__':

    import argparse
    from vbr import tableclasses
    from vbr.client import VBR
    from tapipy.tapis import Tapis

    from .data import data_loads

    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--base-url", help="Tapis API url")
    parser.add_argument("-u", "--username", help="Tapis username")
    parser.add_argument("-p", "--password", help="Tapis password")
    args = parser.parse_args()

    main(vars(args))
