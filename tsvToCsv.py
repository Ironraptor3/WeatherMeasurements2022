import sys

def main(infile, outfile):
    for line in infile:
        outfile.write(line.replace('\t', ',')) # Separate on commas

if __name__ == '__main__':
    if len(sys.argv) > 2:
        with open(sys.argv[1], 'r') as infile:
            with open(sys.argv[2], 'w') as outfile:
                main(infile, outfile)