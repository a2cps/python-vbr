import argparse
import os

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--base-url", 
                        default=os.environ.get('A2CPS_API'), 
                        help="Tapis API url [$A2CPS_API]")
    parser.add_argument("-u", "--username", 
                        default=os.environ.get('A2CPS_USERNAME'), 
                        help="Tapis username [$A2CPS_USERNAME]")
    parser.add_argument("-p", "--password", 
                        default=os.environ.get('A2CPS_PASSWORD'), 
                        help="Tapis password [$A2CPS_PASSWORD]")
    return parser
