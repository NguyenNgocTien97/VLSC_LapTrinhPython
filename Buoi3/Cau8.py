# Cho mảng:
# arr = np.array([10, 25, 30, 45, 50, 65, 70])
# 1. Thay các phần tử nhỏ hơn 30 bằng 0.
# 2. Thay các phần tử lớn hơn 60 bằng 100.
# 3. In mảng sau khi cập nhật.

from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([10, 25, 30, 45, 50, 65, 70])
print(arr)

print(np.where(arr < 30, 0, arr)) # thay các phần tử nhỏ hơn 30 bằng 0
print(np.where(arr > 60, 100, arr)) # thay các phần tử lớn hơn 60 bằng 100
