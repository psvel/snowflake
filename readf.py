import sys
import csv
with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(readCSV)
    for row in readCSV:
        if row:
            print(row[0],row[1])
            print(row)

