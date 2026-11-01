# Cho mảng [3, 7, 3, 9, 7, 3, 5, 9, 3]. Tìm các giá trị duy nhất, số lần xuất hiện của từng giá trị và giá trị xuất hiện nhiều nhất.


import numpy as np

arr = np.array([3, 7, 3, 9, 7, 3, 5, 9, 3])
print("Mang ban dau:", arr)

gia_tri = np.unique(arr)
print("Cac gia tri duy nhat:", gia_tri)

so_lan = np.array([np.count_nonzero(arr == x) for x in gia_tri])
print("So lan xuat hien:", so_lan)

vi_tri = np.argmax(so_lan)
print("Gia tri xuat hien nhieu nhat:", gia_tri[vi_tri])
print("So lan xuat hien nhieu nhat:", so_lan[vi_tri])
