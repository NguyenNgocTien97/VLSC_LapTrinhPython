# Doanh thu 3 ngày đầu tuần là [200, 180, 250], 3 ngày tiếp theo là [0, 220, 270]. Nối hai mảng. Xóa phần tử tại index 3 (ngày nghỉ, thu bằng 0). Chèn thu thứ bảy bằng 300 vào cuối mảng. Tính tổng doanh thu, doanh thu lũy kế và mức tăng hoặc giảm giữa hai ngày liên tiếp.
from numpy import random
import numpy as np
print(np.__version__)

dau_tuan = np.array([200, 180, 250])
tiep_theo = np.array([0, 220, 270])

week = np.concatenate((dau_tuan, tiep_theo)) # nối hai mảng
print("Mang sau khi noi:", week)

week = np.delete(week, 3) # xóa phần tử tại index 3
print("Mang sau khi xoa phan tu tai index 3:", week)

week = np.append(week, 300) # chèn thu thứ bảy bằng 300 vào cuối mảng
print("Mang sau khi them thu bay:", week)

print("Tong doanh thu:", np.sum(week)) # tính tổng doanh thu
print("Doanh thu luy ke:", np.cumsum(week)) # tính doanh thu lũy kế
print("Muc tang hoac giam giua hai ngay lien tiep:", np.diff(week)) # tính mức tăng hoặc giảm giữa hai ngày liên tiếp