# 5. Bài 5 — Xử lý điểm thang 10 (2 điểm)
# Cho mảng [8.34, 10.5, -1, 6.48, 4.96, 7, 3.21]. Giới hạn điểm trong khoảng 0-10, làm tròn đến 1 chữ số thập phân. Sau đó xếp loại theo điểm đã làm tròn: từ 8.0 trở lên là Giỏi, từ 6.5 đến dưới 8.0 là Khá, từ 5.0 đến dưới 6.5 là Trung bình, dưới 5.0 là Yếu.

import numpy as np
print(np.__version__)

diem = np.array([8.34, 10.5, -1, 6.48, 4.96, 7, 3.21])
print(diem)

diem = np.clip(diem, 0, 10)
print(diem)

diem = np.round(diem, 1)
print(diem)

for diem in diem:
    if diem >= 8.0:
        print("Gioi")
    elif diem >= 6.5:
        print("Kha")
    elif diem >= 5.0:
        print("Trung binh")
    else:
        print("Yeu")