import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])

print("copy: ")
x = arr1.copy()
x[0] = 10
print(x)
print(arr1)
print(x.base)

arr2 = np.array([1, 2, 3, 4, 5])
print("view")
y = arr2.view()
y[0] = 10
print(y)
print(arr2)
print(y.base)
