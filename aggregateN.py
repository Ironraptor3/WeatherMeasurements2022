import sys

startRow = 52 # First full day
startCol = 1 # Second column (After date)

def main(filein, fileout, n):

    row = 0
    placeholder = []
    
    for line in filein:
        if row == 0:
            fileout.write(line) # Write header
        elif row < startRow:
            pass # Cut off for convenience
        else:
            values = line.strip('\n').split(',')
            if (row-startRow) % n == 0:
                placeholder = values
                for c in range(startCol, len(values)):
                    placeholder[c] = float(placeholder[c])
            else:
                print(values)
                for c in range(startCol, len(values)):
                    print(float(values[c]))
                    placeholder[c] += float(values[c])
                
                if (row-startRow) % n == (n-1):
                    for c in range(startCol, len(values)):
                        placeholder[c] = str( placeholder[c] / n) # / n for average
                    fileout.write(','.join(placeholder) + '\n')
        row+=1
    
if __name__ == "__main__":
    if len(sys.argv) > 3:
        with open(sys.argv[1], 'r') as filein:
            with open(sys.argv[2], 'w') as fileout:
                main(filein, fileout, int(sys.argv[3]))