import numpy as ns

arr = ns.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr.shape)
# print(arr.reshape(3,3).base)
x = arr.reshape(3, 3)
print(x)
print(x.base)

print("2nd section\n")

arr = ns.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr.reshape(2, 3, -1))
print(arr.reshape(2, 3, -1).base)
print(arr.reshape(2, 3, -1).shape)
