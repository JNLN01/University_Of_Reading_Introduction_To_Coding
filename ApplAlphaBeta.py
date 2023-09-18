import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from scipy import stats

df = pd.read_csv('AAPLNASDAQ.csv')

#To get the statitiscs of the line regression

rl = stats.linregress(df['APPL Returns'], df['NASDAQ Returns'])

print('The Alpha is: ',rl.intercept)
print('The Beta is: ',rl.slope)

#a = 0.002 = Intercept
#b = 1.311 = Slope
#e = 0.336 = Stdeer

