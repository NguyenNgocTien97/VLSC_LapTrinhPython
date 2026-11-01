# Cho mảng:
# scores = np.array([-10, 25, 60, 85, 105, 70])
# 1. Giới hạn điểm trong khoảng 0–100.
# 2. In mảng sau khi xử lý.
# 3. Đếm số giá trị ban đầu nhỏ hơn 0.
# 4. Đếm số giá trị ban đầu lớn hơn 100.
# 5. Gợi ý: np.clip(), Boolean indexing.

from numpy import random
import numpy as np
print(np.__version__)

scores = np.array([-10, 25, 60, 85, 105, 70])
print(scores)

print(np.clip(scores, 0, 100)) # giới hạn điểm trong khoảng 0-100
print(np.sum(scores < 0)) # đếm số giá trị ban đầu nhỏ hơn 0
print(np.sum(scores > 100)) # đếm số giá trị ban đầu lớn hơn 100