# Cho mảng:
# arr = np.array([15, 30, 45, 30, 60, 30, 75])
# 1. Tìm vị trí xuất hiện đầu tiên của giá trị 30.
# 2. Tìm tất cả vị trí xuất hiện của giá trị 30.
# 3. Đếm số lần xuất hiện của giá trị 30.

from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([15, 30, 45, 30, 60, 30, 75])
print(arr)

print(np.where(arr == 30)) # tìm tất cả vị trí xuất hiện của giá trị 30
print(np.where(arr == 30)[0][0]) # tìm vị trí xuất hiện đầu tiên của giá trị 30
print(np.where(arr == 30)[0].size) # đếm số lần xuất hiện của giá trị 30