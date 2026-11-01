# Doanh thu trong 5 ngày là [100, 150, 120, 200, 180]. Tính tổng doanh thu, doanh thu lũy kế, và mức tăng hoặc giảm giữa hai ngày liên tiếp.
from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([100, 150, 120, 200, 180])
print(arr)

print(np.sum(arr)) # tổng doanh thu
print(np.cumsum(arr)) # doanh thu lũy kế
print(np.diff(arr)) # mức tăng hoặc giảm giữa hai ngày liên tiếp