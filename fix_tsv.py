''' Removes columns from the given tsv file and removes commas'''
import argparse
import sys

def main(filein, args):
    '''Performs main function'''
    for line in filein:
        # Split by tab, remove newline
        values = line.strip('\n').split('\t')[args.startcol:]
        if args.endcol > 0:
            # Cut off end if necessary
            values = values[:min(len(values), args.endcol)]
        values = [value.replace(',', '') for value in values]
        args.fileout.write( (','.join(values)+'\n') )

def feed_main():
    '''Sets up for main by parsing parguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--filein', required=True, action='store',
                        help='Path to data file input')
    parser.add_argument('--fileout', action='store', default=sys.stdout,
                        help='Path to data file output')
    parser.add_argument('--startcol', action='store', type=int, default=1,
                        help='The column to start at')
    parser.add_argument('--endcol', action='store', type=int, default=-1,
                        help='The column to end at, -1 for last column')
    args = parser.parse_args()

    close = False
    if isinstance(args.fileout, str):
        # Open the output file if necessary
        args.fileout = open(args.fileout, 'w')
        close = True
    with open(args.filein, 'r') as filein:
        main(filein, args)
    if close:
        args.fileout.close()

if __name__ == "__main__":
    feed_main()
