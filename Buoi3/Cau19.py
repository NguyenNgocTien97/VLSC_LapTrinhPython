# Một lớp có điểm thi của 15 sinh viên:
# scores = np.array([
#  45, 67, 80, 92, 55,
#  73, 88, 39, 95, 61,
#  70, 84, 50, 77, 90
# ])
# 1. In danh sách điểm ban đầu.
# 2. Tính điểm trung bình của lớp.
# 3. Tìm điểm cao nhất, thấp nhất và vị trí tương ứng.
# 4. Đếm số sinh viên đạt và không đạt, với điểm đạt từ 50 trở lên.
# 5. Lọc danh sách sinh viên có điểm từ 80 trở lên.
# 6. Sắp xếp điểm theo thứ tự giảm dần.
# 7. Tính tỷ lệ sinh viên đạt yêu cầu theo phần trăm.
# 8. Thay các điểm dưới 40 thành 40 và in danh sách sau cập nhật.

from numpy import random
import numpy as np
print(np.__version__)

scores = np.array([
 45, 67, 80, 92, 55,
 73, 88, 39, 95, 61,
 70, 84, 50, 77, 90
])
print(scores)

print(np.mean(scores)) # điểm trung bình
print(np.max(scores)) # điểm cao nhất
print(np.min(scores)) # điểm thấp nhất
print(np.sum(scores >= 50)) # đếm số sinh viên đạt điểm từ 50 trở lên
print(np.sum(scores >= 80)) # đếm số sinh viên đạt điểm từ 80 trở lên
print(np.sort(scores)[::-1]) # sắp xếp điểm giảm dần
print(np.sum(scores >= 50) / scores.size * 100) # tỷ lệ phần trăm sinh viên đạt điểm từ 50 trở lên
print(np.clip(scores, 40, 100)) # thay các điểm dưới 40 thành 40