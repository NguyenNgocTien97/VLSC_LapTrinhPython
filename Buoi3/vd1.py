from numpy import random
import numpy as np
print(np.__version__)

#Tạo 1 mảng với các pt là số 0
arr = np.zeros(5)
print(arr)

# Tạo 1 mảng với các pt là số 1
arr = np.ones(4)
print(arr)

# Tạo 1 mảng với các pt là số 2
arr = np.full(4, 2)
print(arr)

# Tạo mảng với các phần tử là số 3
arr = np.full(4, 3)
print(arr)

# Tạo 1 mảng với arrange - tao 1 dãy số
arr = np.arange(1, 10)
print(arr)

# Tạo 1 dãy số với step: 0 2 4 6 8 10
arr = np.arange(0, 11, 2)
print(arr)

# Tạo 1 dãy số cách đều nhau
arr = np.linspace(0, 10, 5)
print(arr)

# Tạo 1 dãy số nguyên random
arr = random.randint(1, 101, size=5)
print(arr)

# Thao tác với mảng 1 chiều thư viện numpy
arr = np.array([10, 20, 30, 40, 50])
print(arr[0]) #Truy cập pt đầu tiên
print(arr[2]) #Truy cập pt thứ 3
print(arr[-1]) #Truy cập pt cuối cùng
print(arr[arr.size -1]) #Truy cập pt cuối cùng

# Slicing 
arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1 : 4]) #Truy cập từ pt thứ 2 đến pt thứ 4
print(arr[:3]) #Truy cập từ pt đầu tiên đến pt thứ 4
print(arr[3:]) #Truy cập từ pt thứ 4 đến pt cuối cùng
print(arr[::2]) #Truy cập pt đầu tiên đến pt cuối cùng với bước nhảy là 2

# Modifying element
arr = np.array([10, 20, 30, 40, 50, 60])
#Cập nhật pt thứ 2 thành các gt 99
# arr[1] = 99
# print(arr)

arr[1:4] = 0
print(arr)

#arithmetic operation
arr = np.array([10, 20, 30, 40])
print(arr + 5)
print(arr - 5)
print(arr * 2)
print(arr / 10)
print(arr ** 2)

#useful properties - funtions
arr = np.array([10, 20, 30, 40])
print(arr.ndim) # số chiều
print(arr.size) # số phần tử
print(arr.shape) # hình dạng mảng
print(arr.dtype) # kiểu dữ liệu

print(np.sum(arr)) # tổng
print(np.mean(arr)) # trung bình
print(np.min(arr)) # min
print(np.max(arr)) # max
print(np.std(arr)) # độ lệch chuẩn

#filtering e using condition
scores = np.array([45, 60, 75, 85, 95])
# print(scores >= 70) 
# print(scores[scores >= 70]) # loc ra nhung phan tu >= 70
#sắp xếp tăng dần
print(np.sort(scores))
#Sắp xếp giảm dần 
print(np.sort(scores)[::-1])
#Tìm điểm 60 đến 90
print(scores[(scores >= 60) & (scores <= 90)])

scores[scores < 50] = 50
print(scores)

#tìm thoe dk - where
position = np.where(scores >= 80)
print(position)
#Phân loại điểm đạt và chưa đạt
results = np.where(scores >= 80, "Dat", "Chua dat")
print(results)

#Đếm pt thỏa điều kiện
print(np.sum(scores >= 70))
print(np.count_nonzero(scores >= 70))
#lấy các pt duy nhất unique()
arr = np.array([10, 20, 10, 30, 20, 40, 30])
print(np.unique(arr))

#Đếm số lần xuất hiện của pt
values, counts = np.unique(arr, return_counts=True)
print(values)
print(counts)

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])
results = np.concatenate((arr1, arr2))
print(results)

#thêm 1 pt
arr = np.array([10, 20, 30])
results = np.append(arr, 50)
print(results)

#xóa 1 pt
arr = np.array([10, 20, 30, 40, 50])
results = np.delete(arr, 2)
print(results)

#xóa nhiều vị trí
print(np.delete(arr, [0, 2]))

#giới hạn giá trị clip()
'''
đưa các giá trị nhỉ hơn ngưỡng tối thiểu lên cái ngưỡng đó
 và các giá trị lớn hơn ngưỡng tooiis đa xuống ngưỡng đó
'''
scores = np.array([-10, 30, 60, 90, 120])
results = np.clip(scores, 0, 100)
print(results)

#chuyển đổi kiểu dữ liệu
results = arr.astype(float)
print(results)
print(results.dtype)
# hàm làm tròn số
arr = np.array([2.345, 3.687, 4.567])
print(np.round(arr, 2))
print(np.round(arr))