import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}
series = pd.Series(calories)

print(series)
print("Sum:", series.sum())
