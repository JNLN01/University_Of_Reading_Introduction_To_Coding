import pandas as pd
import matplotlib.pyplot as plt

#Reads the csv
df = pd.read_csv('2.german_credit.csv')

#Prints dataframe
print(df)
#Prints the first line as a test.
#print(df.iloc[0])

#Mean of 1000 clients credit amount. Gives avg of the credit per customer.
print('Average credit per customer:', df['credit_amount'].mean())
#Mean of clients age
print('Mean age of customers:', df['age'].mean())
#Maximum credit held by a client.
print('Maximum credit hold by a client:', df['credit_amount'].max())

#df['credit_amount'].plot(style='.')

#plt.close()

#df['age'].plot(style='.')

#plt.close()

#Scatter using two columns instead of just one like above.
df.plot(style='.', x='duration_in_month', y='age')

plt.show()

