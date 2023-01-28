import argparse
import sys

def main(filein, args):
    for line in filein:
        values = line.strip('\n').split('\t')[args.startcol:]
        if args.endcol > 0:
            values = values[:args.endcol]
        values = [value.replace(',', '') for value in values]
        args.fileout.write( (','.join(values)+'\n') )

def feed_main():
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
        args.fileout = open(args.fileout, 'w')
        close = True
    with open(args.filein, 'r') as filein:
        main(filein, args)
    if close:
        args.fileout.close()

if __name__ == "__main__":
    feed_main()
