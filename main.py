from urllib.parse import urlparse
import argparse,sys
from huepy import *

my_parser = argparse.ArgumentParser(description='Url Decomposer')
my_parser.add_argument('-u',metavar='u',type=str,help='Url to be decomposed')
my_parser.add_argument('--query', action='store_true',help='Show Only query part of the Url')
my_parser.add_argument('--hostname', action='store_true',help='Show Only hostname part of the Url')
my_parser.add_argument('--path', action='store_true',help='Show Only path part of the Url')
my_parser.add_argument('--all', action='store_true',help='Show every part of the Url')
args = my_parser.parse_args()

if args.u:
    url = urlparse(args.u)
else:
    args.u = sys.stdin.read()
    if args.u:
        url = urlparse(args.u)

if args.all:
    args.hostname,args.path,args.query=[True]*3

if args.hostname:
    print(red(url.hostname))

if args.path:
    print(yellow(url.path))

if args.query:
    for part in url.query.split('&'):
        unpack = part.split('=')
        if len(unpack)>1: 
            key,data=unpack
            print(f'{bold(blue(key))} = {italic(green(data))}')

