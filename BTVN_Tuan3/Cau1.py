# Cho mảng nhiệt độ 7 ngày [31, 27, 34, 29, 26, 33, 30]. Sắp xếp tăng dần và giảm dần. Tìm nhiệt độ cao nhất, thấp nhất và vị trí (index, tính từ 0) của chúng trong mảng ban đầu.

from numpy import random
import numpy as np
print(np.__version__)

nhiet_do = np.array([31, 27, 34, 29, 26, 33, 30])
print(nhiet_do)

print(np.sort(nhiet_do)) # sắp xếp tăng dần
print(np.sort(nhiet_do)[::-1]) # sắp xếp giảm dần
print(np.max(nhiet_do)) # nhiệt độ cao nhất
print(np.min(nhiet_do)) # nhiệt độ thấp nhất
