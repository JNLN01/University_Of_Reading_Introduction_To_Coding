import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#Creates DF with an x and y value
df = pd.DataFrame({
    'x': [2,3,3,2.2],
    'y': [2,6,10,8],
})

#plot the two figures on the scatter graph
plt.scatter(df['x'], df['y'])

#To test the scatter graph works
#plt.show()

#plots the regression line, matches the dataframe columns of x and y and where the data is coming from - df.
#ci=None = not to plot the confidence interval areas
sns.lmplot(x='x', y='y', data=df, line_kws={'color': 'red'})

#prnts the statistics of the line regression
print(stats.linregress(df['x'], df['y']))



