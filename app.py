import pandas as pd
import matplotlib.pyplot as plt

# reading the database
data = pd.read_csv("gdp-per-capita-in-international-and-market-dollars.csv")

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.show()
