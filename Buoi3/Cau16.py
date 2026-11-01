# Doanh thu trong 7 ngày:
# revenue = np.array([100, 120, 90, 150, 180, 160, 200])
# 1. Tính tổng doanh thu.
# 2. Tính doanh thu lũy kế theo từng ngày.
# 3. Tính mức tăng hoặc giảm so với ngày trước.
# 4. Tìm ngày có doanh thu cao nhất.
# 5. Gợi ý: np.cumsum(), np.diff(), np.argmax().

from numpy import random
import numpy as np
print(np.__version__)

revenue = np.array([100, 120, 90, 150, 180, 160, 200])
print(revenue)

print(np.sum(revenue)) # tổng doanh thu
print(np.cumsum(revenue)) # doanh thu lũy kế
print(np.diff(revenue)) # mức tăng hoặc giảm so với ngày trước
print(np.argmax(revenue)) # tìm ngày có doanh thu cao nhất