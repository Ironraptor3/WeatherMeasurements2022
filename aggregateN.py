'''Run from the command line, combines rows of a csv by summation or averaging'''

import argparse
import sys

def main(filein, args):
    '''Runs aggregate function'''
    row = 0
    placeholder = []
    
    for line in filein:
        if row == 0 or (args.endrow > 0 and row >= args.endrow):
            args.fileout.write(line) # Write header / rest of file
        elif row < args.startrow:
            pass # Cut off for convenience
        else:
            values = line.strip('\n').split(',')
            endcol = len(values)
            if args.endcol > 0: # endcol > 0: see whether values or endcol is smaller
                endcol = min(args.endcol, endcol)
            if (row-args.startrow) % args.grouprows == 0:
                # First row in grouping: replace / init placeholder
                placeholder = values
                for c in range(args.startcol, endcol):
                    placeholder[c] = float(placeholder[c])
            else:
                for c in range(args.startcol, endcol):
                    # Update placeholder values
                    placeholder[c] += float(values[c])

                if (row-args.startrow) % args.grouprows == (args.grouprows-1):
                    # Last row in grouping, push to fileout
                    for c in range(args.startcol, endcol):
                        # Average or sum
                        placeholder[c] = str(placeholder[c] / 
                                             (args.grouprows if args.average else 1))
                    args.fileout.write(','.join(placeholder) + '\n')
        row+=1

def feed_main():
    '''Set up main by parsing arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--filein', required=True, action='store',
                        help='Path to data file input')
    parser.add_argument('--fileout', action='store', default=sys.stdout,
                        help='Path to data file output')
    parser.add_argument('--startrow', action='store', type=int, default=1,
                        help='The row to start at. First full day at 52')
    parser.add_argument('--startcol', action='store', type=int, default=1,
                        help='The column to start at')
    parser.add_argument('--endrow', action='store', type=int, default=-1,
                        help='The row to end at; -1 for end of the file. \
                              3404 is the end of 5 minute intervals')
    parser.add_argument('--endcol', action='store', type=int, default=-1,
                        help='The column to end at, -1 for last column')
    parser.add_argument('--grouprows', action='store', type=int, default=2,
                        help='The number of rows to group together. \
                              144-10 minute intervals in a day')
    parser.add_argument('--average', action='store_true', default=False,
                        help='Specify to average rows instead of add them')
    args = parser.parse_args()

    close = False
    if isinstance(args.fileout, str): # Open the file if necessary
        args.fileout = open(args.fileout, 'w')
        close = True
    with open(args.filein, 'r') as filein:
        main(filein, args)
    if close:
        args.fileout.close()

 
if __name__ == "__main__":
    feed_main()
