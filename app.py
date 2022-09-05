import csv

with open('gdp-per-capita-in-international-and-market-dollars.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
       print(row)