from numpy import random
import numpy as np
print(np.__version__)

# Cho mảng [10, 20, 10, 30, 20, 10, 40]. Tìm các giá trị duy nhất và số lần xuất hiện của từng giá trị.
arr = np.array([10, 20, 10, 30, 20, 10, 40])
print(arr)

print(np.unique(arr)) # tìm các giá trị duy nhất
print(np.unique(arr, return_counts=True)) # tìm các giá trị duy nhất và số lần xuất hiện