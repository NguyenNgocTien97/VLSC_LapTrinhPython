# Cho mảng điểm:
# scores = np.array([45, 78, 90, 55, 62, 88, 35, 95, 70, 48])
# 1. Tính điểm trung bình.
# 2. Đếm số sinh viên đạt điểm từ 50 trở lên.
# 3. Lọc các điểm từ 80 trở lên.
# 4. Tìm điểm cao nhất và thấp nhất.
# 5. Tính tỷ lệ phần trăm sinh viên đạt điểm từ 50 trở lên.

from numpy import random
import numpy as np
print(np.__version__)

scores = np.array([45, 78, 90, 55, 62, 88, 35, 95, 70, 48])
print(scores)

print(np.mean(scores)) # điểm trung bình
print(np.sum(scores >= 50)) # đếm số sinh viên đạt điểm từ 50 trở lên
print(scores[scores >= 80]) # lọc các điểm từ 80 trở lên
print(np.max(scores)) # điểm cao nhất
print(np.min(scores)) # điểm thấp nhất
print(np.sum(scores >= 50) / scores.size * 100) # tỷ lệ phần trăm sinh viên đạt điểm từ 50 trở lên
