# Cho mảng:
# arr = np.array([12, 25, 38, 41, 56, 69])
# 1. In mảng theo thứ tự ngược lại.
# 2. In 3 phần tử cuối theo thứ tự ban đầu.
# 3. In các phần tử ở vị trí chẵn (index chẵn).


from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([12, 25, 38, 41, 56, 69])
print(arr)

print(arr[::-1]) # đảo ngược mảng
print(arr[-3:]) # 3 phần tử cuối
print(arr[::2]) # các phần tử ở vị trí chẵn