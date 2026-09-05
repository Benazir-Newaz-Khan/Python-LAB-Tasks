import pandas as pd

filename = input("Enter the CSV file name: ")
df = pd.read_csv(filename)

print(df.head())
print(df.tail())
df.info()
