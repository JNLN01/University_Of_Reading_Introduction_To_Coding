import pandas as pd
import numpy as np
CustomerName = pd.Series(['May', 'Clarkson', 'Hamond'])

# Create a Pandas Series with all the customer ages
CustomerAge = pd.Series([38, 26, 22])

# Create a Pandas Series with all the branches the accounts were opened
AccountBranch = pd.Series(['London', 'Guangzhou', 'Delhi'])

# Create a Pandas Series with all the account balances
AccountBalance = pd.Series([3682.4, 8954.2, 6357.1])

df = pd.DataFrame({'Name': CustomerName, 'Age': CustomerAge, 'Branch': AccountBranch, 'Balance': AccountBalance})
#prints df
print(df)
#Prints only the row i want, using the dataframe index, this is similar to lists.
print(df.loc[0])
#When wanting a specific Column.
print(df['Age'])
#Slice for AGE column more than 22.
Age2 = df[df['Age'] > 22]

print(np.mean(Age2))
