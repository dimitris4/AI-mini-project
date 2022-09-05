import csv
import pandas as pd
import matplotlib.pyplot as plt

with open('gdp-per-capita-in-international-and-market-dollars.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
       print(row)

# reading the database
data = pd.read_csv("gdp-per-capita-in-international-and-market-dollars.csv")

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()
