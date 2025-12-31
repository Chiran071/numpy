import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])


print(np.concatenate((arr1, arr2)))
print(np.concatenate((arr1, arr2), axis=0))
print()
# 2D
arr1 = np.array([[1, 2, 3, 4]])  # 2d array
arr2 = np.array([[5, 6, 7, 8]])  # 2d array
print(np.concatenate((arr1, arr2), axis=1), "\n")  # concatenate in row
print(np.concatenate((arr1, arr2)))  # concatenate in column, by default axis is 0

# concatenate can't create new dimension can only join array on existing dimension, inorder to create new dimension
