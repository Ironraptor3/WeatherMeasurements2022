import sys

def main(filein, fileout):
    for line in filein:
        values = line.strip('\n').split('\t')[1:]
        values = [value.replace(',', '') for value in values]
        fileout.write( (','.join(values)+'\n') )

if __name__ == "__main__":
    if len(sys.argv) > 2:
        with open(sys.argv[1], "r") as filein:
            with open(sys.argv[2], "w") as fileout:
                main(filein, fileout)