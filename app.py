import pandas as pd
import matplotlib.pyplot as plt

GDP_data = pd.read_csv("gdp-per-capita-in-international-and-market-dollars.csv")
happiness_data = pd.read_csv("happiness-cantril-ladder.csv")

allowed_years = [2008, 2018]
GDP_data = GDP_data[GDP_data['Year'].isin(allowed_years)]
GDP_data['GDP_pct_change_2008-2018'] = GDP_data.groupby('Entity')['GDP per capita (constant 2015 US$)'].pct_change()
GDP_data = GDP_data.dropna()

happiness_data = happiness_data[happiness_data['Year'].isin(allowed_years)]
happiness_data['Happiness_pct_change_2008-2018'] = happiness_data.groupby('Entity')['Life satisfaction in Cantril Ladder (World Happiness Report 2022)'].pct_change()
happiness_data = happiness_data.dropna()

merged_df = pd.merge(GDP_data, happiness_data, on='Entity')
merged_df['GDP_pct_change_2008-2018'] = merged_df['GDP_pct_change_2008-2018'] * 100
merged_df['Happiness_pct_change_2008-2018'] = merged_df['Happiness_pct_change_2008-2018'] * 100

plt.title("Scatter Plot")
plt.xlabel('Change in GDP between 2008-2018')
plt.ylabel('Change in Happiness Index between 2008-2018')
plt.scatter(merged_df['GDP_pct_change_2008-2018'], merged_df['Happiness_pct_change_2008-2018'])
  
for index, row in merged_df.iterrows():
    plt.text(int(row['GDP_pct_change_2008-2018']), int(row['Happiness_pct_change_2008-2018']), row['Entity'])

plt.show()
