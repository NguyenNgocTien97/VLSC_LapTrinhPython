# Cho mảng [42, 67, 85, 51, 73, 98, 60, 39, 80]. In ra các số lớn hơn 50 và không vượt quá 80. Đếm số phần tử thỏa điều kiện và tính trung bình của chúng.
from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([42, 67, 85, 51, 73, 98, 60, 39, 80])
print(arr)

print(arr[(arr > 50) & (arr <= 80)]) # loc ra nhung phan tu > 50 va <= 80
print(np.sum(arr[(arr > 50) & (arr <= 80)])) # dem so phan tu thoa man dieu kien
print(np.mean(arr[(arr > 50) & (arr <= 80)])) # tinh trung binh cac phan tu thoa man dieu kien