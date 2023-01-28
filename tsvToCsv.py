import argparse
import sys

def main(filein, args):
    for line in filein:
        args.fileout.write(line.replace('\t', ',')) # Separate on commas

def feed_main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filein', required=True, action='store',
                        help='Path to data file input')
    parser.add_argument('--fileout', action='store', default=sys.stdout,
                        help='Path to data file output')
    args = parser.parse_args()

    close = False
    if isinstance(args.fileout, str):
        args.fileout = open(args.fileout, 'w')
        close = True
    with open(args.filein, 'r') as filein:
        main(filein, args)
    if close:
        args.fileout.close()

if __name__ == '__main__':
    feed_main()
