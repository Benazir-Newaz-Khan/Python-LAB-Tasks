import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Titanic-Dataset.csv")

numeric = df.select_dtypes(include="number")

plt.plot(numeric.index, numeric["Age"])
plt.title("Titanic Age by Passenger")
plt.xlabel("Passenger Index")
plt.ylabel("Age")
plt.show()

plt.scatter(numeric["Age"], numeric["Fare"])
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

survived = df["Survived"].value_counts().sort_index()
plt.bar(["Did not survive", "Survived"], survived)
plt.title("Titanic Survival")
plt.xlabel("Outcome")
plt.ylabel("Passengers")
plt.show()

plt.hist(df["Age"].dropna(), bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.pie(survived, labels=["Did not survive", "Survived"], autopct="%1.1f%%")
plt.title("Survival Percentage")
plt.show()

fig, ax = plt.subplots(1, 2)
ax[0].hist(df["Fare"], bins=10)
ax[1].scatter(df["Age"], df["Fare"])
plt.show()
