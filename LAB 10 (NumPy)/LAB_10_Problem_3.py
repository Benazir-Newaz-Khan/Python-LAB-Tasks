import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Column sums:", np.sum(arr, axis=0))
print("Row sums:", np.sum(arr, axis=1))
