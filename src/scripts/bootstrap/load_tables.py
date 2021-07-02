def main(args):

    t = Tapis(base_url=args['base_url'],
              username=args['username'],
              password=args['password'])
    v = VBR(tapis_client=t)

    ordered_tables = tableclasses.table_definitions()
    ordered_data = data_loads(ordered_tables)
    for od in ordered_data:
        try:
            v.create(od)
        except Exception as exc:
            print(exc)


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
