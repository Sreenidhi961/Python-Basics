import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("Element at row 1, column 2:", arr[1, 2])
print("Second row:", arr[1,:])
print("Last column:", arr[:, 3])
print("Sub-array:")
print(arr[0:2, 1:3])
