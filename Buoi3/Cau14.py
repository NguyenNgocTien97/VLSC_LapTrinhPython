# Cho mảng:
# arr = np.array([12, 25, 37, 48, 59, 72, 85])
# 1. Tìm phần tử gần với số 50 nhất.
# 2. Tìm phần tử gần với số 70 nhất.
# 3. In ra giá trị và vị trí tương ứng.
# 4. Gợi ý: np.abs() và np.argmin().

from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([12, 25, 37, 48, 59, 72, 85])
print(arr)

print(np.abs(arr - 50))
print(np.argmin(np.abs(arr - 50))) # vị trí phần tử gần với số 50 nhất
print(np.abs(arr - 70))
print(np.argmin(np.abs(arr - 70))) # vị trí phần tử gần với số 70 nhất