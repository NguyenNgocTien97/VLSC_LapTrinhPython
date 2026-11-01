# Cho mảng điểm [78, 55, 90, 65, 88, 45]. Sắp xếp tăng dần và giảm dần; tìm điểm cao nhất, thấp nhất và vị trí của chúng.
from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([78, 55, 90, 65, 88, 45])
print(arr)

print(np.sort(arr)) # tăng dần
print(np.sort(arr)[::-1]) # giảm dần
print(np.max(arr)) # max
print(np.min(arr)) # min