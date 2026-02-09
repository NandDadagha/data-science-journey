# This script demonstrates properties of NumPy arrays, including their shape.

import numpy as np
arr = np.array([5, 10, 15, 20, 25])

print("Array:", arr)
print("Shape of the array:", arr.shape)
print("Size of the array:", arr.size)
print("Dimensions of the array:", arr.ndim)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Matrix:")
print(matrix)
print("Shape of the matrix:", matrix.shape)
print("Size of the matrix:", matrix.size)
print("Dimensions of the matrix:", matrix.ndim)