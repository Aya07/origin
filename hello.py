import pandas as pd
import matplotlib.pyplot as plt 
df = pd.read_csv('./avocado.csv')
first3lines = df.head()
print(first3lines)
print(df.tail(2))
print(df['Small Bags'].head())
print(df.AveragePrice.head())
albany_df = df[df['region'] == 'Albany']
print(albany_df)
print(albany_df.index)



def foo():
    return 5










