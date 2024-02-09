'''
Supplement to aggregateN.py; used to grab a specific interval of data,
which will then be fed into aggregateN.
For example, one may specify the range 10am - 2 pm within the arguments
(corresponding to the 10am - 2pm rows) and all data will be removed cleanly
aside from 10 am - 2 pm values.
'''

import argparse
import os
import sys

def main(args):
    row = 0

    for line in args.filein:
        if args.startcol > 0 or args.endcol > 0:
            line = line.rstrip().split(',')[args.startcol:]
            if args.endcol > 0:
                line = line[:args.endcol]
            line = '%s\n' % ','.join(line)

        if args.endrow > 0 and row >= args.endrow:
            break # End early
        elif row != 0 and (row < args.startrow or (row-args.startrow) % args.interval >= args.include):
            pass # Ignore this line
        else:
            args.fileout.write(line) # Able to write this line
        row += 1
    # Broke early or reached EOF here

def feed_main():
    ''' Set up main parsing arguments, should be similar to aggregateN'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--filein', type=argparse.FileType('r'),
                        required=True, action='store',
                        help='Path to data file input')
    parser.add_argument('--fileout', action='store', default=sys.stdout,
                        help='Path to data file output')
    parser.add_argument('--startrow', action='store', type=int, default=121,
                        help='The row to start at. Default = 121 (10 am w/ 5 minute increments)')
    parser.add_argument('--endrow', action='store', type=int, default=-1,
                        help='The row to end at; -1 for end of the file (Default).')
    parser.add_argument('--startcol', action='store', type=int, default=0,
                        help='Starting column to extract. Default = 0 (first column)')
    parser.add_argument('--endcol', action='store', type=int, default=-1,
                        help='Ending column to extract. Default = -1 (Special value to use all)')
    parser.add_argument('--interval', action='store', type=int, default=288,
                        help='The interval for each inclusion. Defaults to 1 day = '
                        '288 (assuming 5 minute measurements)')
    parser.add_argument('--include', action='store', type=int, default=48,
                        help='Number of rows to include in each interval. '
                        'Defaults to 10am-2pm = 48 (assuming 5 minute measurements)')
    args = parser.parse_args()

    close = False
    if isinstance(args.fileout, str):
        dirname = os.path.dirname(args.fileout)
        if not os.path.exists(dirname):
            os.makedirs(dirname, exist_ok=True)
        args.fileout = open(args.fileout, 'w')
        close = True

    main(args)

    if close:
        args.fileout.close()

if __name__ == '__main__':
    feed_main()

