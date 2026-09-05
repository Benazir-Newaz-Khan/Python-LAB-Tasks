import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([10, 25, 30, 50])

print(np.where(arr1 == arr2)[0])
