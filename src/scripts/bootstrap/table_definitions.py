import json
from vbr import tableclasses


def main():
    defs = tableclasses.table_definitions()
    print(json.dumps(defs, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
