import argparse
import logging
import sys
from typing import List, Optional

LOG_FILENAME = 'libscARM-tracebacks.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

def parse_args(argv: List[str]):
    description = '''
       Starts the command line interface of libsc
       '''
    formatter_class = argparse.RawDescriptionHelpFormatter
    
    parser = argparse.ArgumentParser(description=description,
                                     formatter_class=formatter_class)

    parser.add_argument('-v',
                        '--version',
                        action='store_true',
                        help='Print the version of the cli.') 
    
    parser.add_argument('-i',
                        '--init',
                        action='store_true',
                        default=False,
                        help='Set up the test environment.')
   
    parser.add_argument('-l',
                        '--load',
                        action='store_true',
                        default=False,
                        help='Load the test suite.')
   
    parser.add_argument('--run',
                        action='store_true',
                        default=False,
                        help='Run L1 and L2 cache tests.')
   
    return parser.parse_args(argv)


def main(options: Optional[List[str]]=None):
    '''
    Launch terminal interface
    '''

    argv = options if options is not None else sys.argv[1:]
    args = parse_args(argv)

    if args.version:
        print('libscARM 0.0.1')

    if args.init:
        print('Running init script')

    if args.load:
        print('Loading test suite')

    if args.run:
        print('Running test suite')

    if args.run:
        print('Generating test report')


if __name__=='__main__':
    main()
