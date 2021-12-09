def main(args):

    t = Tapis(
        base_url=args["base_url"], username=args["username"], password=args["password"]
    )
    t.get_tokens()
    v = VBR(tapis_client=t)

    if len(args["table_id"]) > 0:
        to_drop = args["table_id"]
    else:
        to_drop = [t["table_id"] for t in v.list_tables()]

    for t in to_drop:
        print("Deleting {0}".format(t))
        try:
            v.delete_table(t)
        except Exception as exc:
            print(exc)


if __name__ == "__main__":

    from tapipy.tapis import Tapis

    from vbr import tableclasses
    from vbr.client import VBR

    from .cli import get_parser
    from .data import data_loads

    parser = get_parser()
    parser.add_argument("table_id", nargs="*", help="Optional: Table ID(s)")
    args = parser.parse_args()

    main(vars(args))
