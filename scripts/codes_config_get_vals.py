#!/usr/bin/python2.7
import argparse
import sys
from itertools import islice

import configurator as conf

def main():
    args = parse_args()

    mod = conf.import_from(args.substitute_py)

    conf.check_cfields(mod)
    
    for pair in mod.cfields:
        if pair[0] == args.token:
            sys.stdout.write(str(pair[1][0]))
            for x in islice(pair[1],1,None):
                sys.stdout.write(" " + str(x))
            sys.stdout.write('\n')
            sys.exit(0) # success
    else: # failure, did not find
        raise ValueError('could not find token "' + args.token + '"')
        

def parse_args():
    parser = argparse.ArgumentParser(\
            description="echo the values of a token file to stdout")
    parser.add_argument("substitute_py",
            help='python file defining "cfields" variable consisting of '
                 'elements of the form '
                 '( replacement_token, [replacements...])')
    parser.add_argument("token",
            help="replacement token to print values out for")
    return parser.parse_args()

if __name__ == "__main__":
    main()
