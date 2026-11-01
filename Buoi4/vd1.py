import pandas as pd

# print(pd.__version__)

df = pd.read_csv("D:\DataMining\Buoi4\data.csv", encoding="utf-8")
print(df)

#xem 5 dong dau tien
print(df.head())

#xem 5 dong cuoi cung 
print(df.tail())

#xem kich thuoc du lieu
print(df.shape)

#xem ten cot
print(df.columns)

#xem thong tin tong quat
print(df.info())

#xem du lieu
print(df.dtypes)
print(df.describe())

# Phát hiện dữ liệu bị thiếu
print(df.isna().sum().sum())

# lọc các dòng bị thiếu
missing_row = df[df.isna().any(axis=1)]
print(missing_row)

# xóa dòng dữ liệu bị thiếu
df_drop = df.dropna()
print(df_drop)

# thay thế dữ liệu bị thiếu
df["Python"] = df["Python"].fillna(df["Python"].mean())
print(df)

# phát hiện dữ liệu sai - dữ liệu bất thường
'''
Tuoi sv: 16 - 100
Diem Python & pandas: 0 - 100
Chuyen can: 0 - 100
'''

invalid_age = df [
    (df["Age"] < 16) | (df["Age"] > 100)
]
print(invalid_age)

# Tìm điểm ko hợp lệ - pandas
invalid_pandas = df [
    ((df["Pandas"] < 0) | (df["Pandas"] > 100))
]
print(invalid_pandas)

# Tìm điểm ko hợp lệ - attendnce
invalid_attendance = df [
    ((df["Attendance"] < 0) | (df["Attendance"] > 100))
]
print(invalid_attendance)

# lam sach du lieu bi sao
import numpy as np
df.loc[
    (df["Age"] < 16) | (df["Age"] > 100), "Age"
] = np.nan

df.loc[
    (df["Python"] < 0) | (df["Python"] > 100), "Python"
] = np.nan

df.loc[
    (df["Pandas"] < 0) | (df["Pandas"] > 100), "Pandas"
] = np.nan

df.loc[
    (df["Attendance"] < 0) | (df["Attendance"] > 100), "Attendance"
] = np.nan

print(df.isna().sum())
# chuan hoa du lieu
df["Name"] = df["Name"].str.strip()
print(df["Name"])

# Chuan hoa ten lop
df["Class"] = df["Class"].str.strip().str.upper()
print(df["Class"].unique())

# tim du lieu bi trung lap
print(df.duplicated().sum())

# Kiem tra mssv bi trung ko
print(df[df.duplicated(subset=["StudentID"],keep=False)])

# xu ly du lieu bi thieu sau khi lam sach
# chuen gia tri NaN sang 1 gia tri thay the

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Python"] = df["Python"].fillna(df["Python"].median())
df["Pandas"] = df["Pandas"].fillna(df["Pandas"].median())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())

# Kiem tra lai
print(df.isna().sum())
print(df)

# tinh toan va phan tich
df["Average"] = (df["Python"] + df["Pandas"]) / 2
print(df)

# phan loai kq
df["Results"] = df["Average"].apply(
    lambda score: "Pass" if score >= 70 else "Fail")
print(df)

# loc cac sinh vien dat
passed = df[df["Results"] == "Pass"]
print(passed)

# sap xep theo diem tb
df_sorted = df.sort_values(by="Average", ascending=False)
print(df_sorted)

# thong ke tong quan
print("Average Python: ", df["Python"].mean())
print("Average Pandas: ", df["Pandas"].mean())
print("Highest average: ", df["Average"].max())
print("Lowest average: ", df["Average"].min())

# xuat du lieu sau khi xu ly
df.to_csv("student_clean.csv", index=False, encoding="utf-8-sig")