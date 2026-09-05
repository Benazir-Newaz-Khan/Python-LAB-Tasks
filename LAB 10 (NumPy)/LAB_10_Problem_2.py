import numpy as np

arr = np.array([10, 20, 10, 30, 10, 20, 40])
value = int(input("Enter the item: "))
n = int(input("Enter the repetition number: "))

positions = np.where(arr == value)[0]

if n <= len(positions):
    print(positions[n - 1])
else:
    print("The item does not repeat that many times.")
