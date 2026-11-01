# Cho mảng:
# arr = np.array([12, 7, 24, 31, 46, 53, 60, 75])
# 1. Tạo mảng chỉ chứa số chẵn.
# 2. Tạo mảng chỉ chứa số lẻ.
# 3. Đếm số lượng số chẵn và số lượng số lẻ.

from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([12, 7, 24, 31, 46, 53, 60, 75])
print(arr)

print(arr[arr % 2 == 0]) # tạo mảng chỉ chứa số chẵn
print(arr[arr % 2 != 0]) # tạo mảng chỉ chứa số lẻ
print(np.sum(arr % 2 == 0)) # đếm số chẵn
print(np.sum(arr % 2 != 0)) # đếm số lẻ
