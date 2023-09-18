import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Reads the csv and saves as a dataframe
df = pd.read_csv('storedata_proper.csv')

#Test to see the df
#print(df)

#prints the first line of the csv
#print(df.iloc[0])

df['ordfreq'].mean()

df['ordfreq'].median()

df['ordfreq'].max()

#Regression line - turned off scatter as to many datapoints
sns.lmplot(x='eclickrate', y='ordfreq', data=df, scatter=False)

#prints the statisitics of the regression line
print(stats.linregress(df['eclickrate'], df['ordfreq']))
#Slope = a
#Intercept = B
#Stdeer = E
# Regression Line = A + Bx + E
plt.show()