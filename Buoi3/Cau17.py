# Cho mảng:
# arr = np.array([20, 40, 60, 80, 100])
# 1. Tính giá trị nhỏ nhất và lớn nhất.
# 2. Chuẩn hóa từng giá trị theo công thức x' = (x - xmin) / (xmax - xmin).
# 3. In mảng sau khi chuẩn hóa.
# 4. Giá trị sau chuẩn hóa nằm trong khoảng từ 0 đến 1.

from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([20, 40, 60, 80, 100])
print(arr)

print(np.min(arr)) # giá trị nhỏ nhất
print(np.max(arr)) # giá trị lớn nhất
print((arr - np.min(arr)) / (np.max(arr) - np.min(arr))) # chuẩn hóa mảng
print(np.min((arr - np.min(arr)) / (np.max(arr) - np.min(arr)))) # giá trị nhỏ nhất sau chuẩn hóa
print(np.max((arr - np.min(arr)) / (np.max(arr) - np.min(arr)))) # giá trị lớn nhất sau chuẩn hóa