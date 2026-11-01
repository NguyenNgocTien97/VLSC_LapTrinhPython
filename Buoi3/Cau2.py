# Cho mảng [35, 60, 75, 45, 90, 80, 50]. In ra các số từ 50 đến dưới 80, sau đó đếm số phần tử thỏa mãn điều kiện.
from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([35, 60, 75, 45, 90, 80, 50])
print(arr)

print(arr[(arr >= 50) & (arr < 80)]) # loc ra nhung phan tu >= 50 va < 80
print(np.sum(arr[(arr >= 50) & (arr < 80)])) # dem so phan tu thoa man dieu kien
