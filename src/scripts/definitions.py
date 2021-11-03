def main():

    import argparse
    import json
    import os
    from vbr import tableclasses

    tdefs = tableclasses.table_definitions()
    for td in tdefs:
        fname = td['table_name'] + '.json'
        with open(fname, 'w') as file:
            json.dump(td, file, sort_keys=True, indent=4)
            print(td['table_name'])


if __name__ == '__main__':
    main()
