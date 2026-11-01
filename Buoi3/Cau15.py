# Cho hai mảng:
# arr1 = np.array([10, 20, 30, 40])
# arr2 = np.array([30, 40, 50, 60])
# 1. Nối hai mảng thành một mảng mới.
# 2. Tìm các giá trị xuất hiện trong cả hai mảng.
# 3. Tạo mảng chứa tất cả giá trị không trùng lặp của hai mảng.
# 4. Sắp xếp kết quả tăng dần.
# 5. Gợi ý: np.concatenate(), np.intersect1d(), np.union1d().

from numpy import random
import numpy as np
print(np.__version__)

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([30, 40, 50, 60])
print(arr1)
print(arr2)

print(np.concatenate((arr1, arr2))) # nối hai mảng
print(np.intersect1d(arr1, arr2)) # tìm các giá trị xuất hiện trong cả hai mảng
print(np.union1d(arr1, arr2)) # tạo mảng chứa tất cả giá trị không trùng lặp của hai mảng