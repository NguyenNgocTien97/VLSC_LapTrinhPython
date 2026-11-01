# Cho mảng [45, 120, -5, 75, 95, 60]. Giới hạn điểm trong khoảng 0–100, làm tròn đến số nguyên nếu cần, rồi phân loại điểm từ 50 trở lên là Đạt, còn lại là Không đạt.
from numpy import random
import numpy as np
print(np.__version__)

arr = np.array([45, 120, -5, 75, 95, 60])
print(arr)

print(np.clip(arr, 0, 100)) # giới hạn điểm trong khoảng 0-100
print(np.round(arr)) # làm tròn đến số nguyên
print(np.where(arr >= 50, "Dat", "Khong dat")) # phân loại điểm Đạt hoặc Không đạt