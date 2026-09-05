import pandas as pd

filename = input("Enter the Titanic CSV file name: ")
df = pd.read_csv(filename)

for column in ["Age", "Fare", "SibSp", "Parch"]:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

if "Age" in df.columns:
    df.loc[df["Age"] < 0, "Age"] = pd.NA
    df["Age"] = df["Age"].fillna(df["Age"].median())

if "Fare" in df.columns:
    df.loc[df["Fare"] < 0, "Fare"] = pd.NA
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

if "Embarked" in df.columns:
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop_duplicates()
df = df.dropna()

print(df.head())
df.to_csv("titanic_cleaned.csv", index=False)
