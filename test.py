import pandas as pd

df = pd.read_csv('transactions.csv')

print(sum(df['currency'] != "RUB"))

# print(df)