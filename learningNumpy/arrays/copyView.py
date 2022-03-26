import numpy as np

arr = np.array([1, 2, 3, 4])

x = arr.copy()
arr[0] = 30

print(arr)
print(x)

print()

y = arr.view()
arr[0] = 43

print(y)
print(arr)