# Cho mảng:
# arr = np.array([12, 18, 25, 30, 42, 55])
# 1. Kiểm tra tất cả phần tử có lớn hơn 10 hay không.
# 2. Kiểm tra có phần tử nào lớn hơn 50 hay không.
# 3. Kiểm tra tất cả phần tử có nằm trong khoảng từ 10 đến 60 hay không.
# 4. Gợi ý: np.all(), np.any().

from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([12, 18, 25, 30, 42, 55])
print(arr)

print(np.all(arr > 10)) # kiểm tra tất cả phần tử có lớn hơn 10 hay không
print(np.any(arr > 50)) # kiểm tra có phần tử nào lớn hơn 50 hay không
print(np.all((arr >= 10) & (arr <= 60))) # kiểm tra tất cả phần tử có nằm trong khoảng từ 10 đến 60 hay không
