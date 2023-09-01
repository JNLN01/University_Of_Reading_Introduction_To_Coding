import pandas as pd
import numpy as np

CapitalCities = pd.Series(['Washington', 'Madrid', 'Beijing'])
PopulationMillions = pd.Series([0.7, 3.2, 21.7])
FoundedIn = pd.Series([1791, 899, 1403])

df = pd.DataFrame({'Capital Cities': CapitalCities, 'Population in Millions': PopulationMillions,
                   'City Founded In': FoundedIn})

#print(df)

LowestPopulation = PopulationMillions.min()

df1 = df[df['Population in Millions'] <= LowestPopulation]

print(df1)

print('Population mean: ', np.mean(PopulationMillions))
MaximumPopulation = PopulationMillions.max()
print('Maximum Population:', MaximumPopulation)



