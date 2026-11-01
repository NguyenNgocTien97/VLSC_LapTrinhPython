# Tạo hai mảng [1, 2, 3] và [4, 5, 6]. Nối hai mảng, thêm số 7 vào mảng kết quả và xóa phần tử tại index 2.

from numpy import random
import numpy as np
print(np.__version__)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)

print(np.concatenate((arr1, arr2))) # nối hai mảng

arr3 = np.append(arr1, 7) # thêm số 7 vào mảng kết quả
print(arr3)

print(np.delete(arr3, 2)) # xóa phần tử tại index 2