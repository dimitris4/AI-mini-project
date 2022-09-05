import pandas as pd
import matplotlib.pyplot as plt

# reading the database
GDP_data = pd.read_csv("gdp-per-capita-in-international-and-market-dollars.csv")
happiness_data = pd.read_csv("happiness-cantril-ladder.csv")

# print(GDP_data)
# print(happiness_data)

allowed_years = [2008, 2018]
GDP_data = GDP_data[GDP_data['Year'].isin(allowed_years)]
GDP_data['GDP_pct_change_2008-2018'] = GDP_data.groupby('Entity')['GDP per capita (constant 2015 US$)'].pct_change()
GDP_data = GDP_data.dropna()

happiness_data = happiness_data[happiness_data['Year'].isin(allowed_years)]

print(happiness_data)
#print(GDP_data)

# # Adding Title to the Plot
# plt.title("Scatter Plot")

# # Setting the X and Y labels
# plt.xlabel('Change in GDP between 2008-2018')
# plt.ylabel('Change in Happiness Index between 2008-2018')

# plt.show()
