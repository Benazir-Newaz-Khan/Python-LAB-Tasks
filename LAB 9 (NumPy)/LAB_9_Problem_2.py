import numpy as np

arr = np.array([10, 20, 30, 20, 50])
value = int(input("Enter the value to search: "))

print(np.where(arr == value))
