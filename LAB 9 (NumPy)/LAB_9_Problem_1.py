import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print(arr.reshape(rows, columns))
