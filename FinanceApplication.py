import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv('stocktencent.csv')

print(df)

StockReturn = (df['TencReturns'][1]/df['TencReturns'][0]) - 1

print(StockReturn)

# The above works but i dont think the actual calculation use is correct.

df['TencReturns'].mean()

df['TencReturns'].median()

df['TencReturns'].max()

#Scatter for stock returns
#plt.scatter(x='Month', y='TencReturns', data=df)

#Scatter for HS index return
#plt.scatter(x='Month', y='HSReturns', data=df)

#Simple Market Model Regression
#Requires regression analysis on both the stock and HS index
sns.regplot(x='HSReturns', y='TencReturns', data=df)

#Add the line to represent perfectly balanced stock and index
sns.lineplot(x=[-0.100, 0.100], y=[-0.100, 0.100],
linestyle=':', color='red', linewidth=4 )

plt.show()

#Statistics of the regression line.
print(stats.linregress(df['HSReturns'], df['TencReturns']))

#a = 0.002 = Intercept
#b = 1.311 = Slope
#e = 0.336 = Stdeer


