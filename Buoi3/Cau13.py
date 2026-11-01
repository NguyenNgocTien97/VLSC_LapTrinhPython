# Cho mảng mã sản phẩm:
# products = np.array([101, 102, 101, 103, 102, 104, 101, 103])
# 1. Liệt kê các mã sản phẩm không trùng lặp.
# 2. Đếm số lần xuất hiện của từng mã.
# 3. Tìm mã xuất hiện nhiều lần nhất.
# 4. Gợi ý: np.unique(..., return_counts=True).

from numpy import random
import numpy as np
print(np.__version__)

products = np.array([101, 102, 101, 103, 102, 104, 101, 103])
print(products)

print(np.unique(products)) # liệt kê các mã sản phẩm không trùng lặp
print(np.unique(products, return_counts=True)) # đếm số lần xuất hiện của từng mã
print(np.where(products == np.max(products))[0][0]) # tìm mã xuất hiện nhiều lần nhất
