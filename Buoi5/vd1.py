import pandas as pd
import numpy as np

df = pd.read_csv(r"d:\DataMining\Buoi5\sales_practice_dataset.csv", encoding="utf-8-sig")

# Bước 1. Khám phá dữ liệu
print(df.head())
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())

# Bước 2. Kiểm tra dữ liệu thiếu
print(df.isna().sum())
print("Tổng ô thiếu:", df.isna().sum().sum())

missing_rows = df[df.isna().any(axis=1)]
print(missing_rows)

# Bước 3. Chuẩn hóa văn bản
df["Product"] = df["Product"].str.strip()
df["City"] = df["City"].str.strip()
df["Category"] = df["Category"].str.strip()

print(df["Product"].unique())
print(df["City"].unique())

# Bước 4. Phát hiện giá trị không hợp lệ
print(df[df["Quantity"] <= 0])
print(df[df["UnitPrice"] <= 0])
print(df[df["Quantity"] > 50])

invalid = df[
    (df["Quantity"] <= 0) |
    (df["UnitPrice"] <= 0)
]
print(invalid)

# Bước 5. Phát hiện ngoại lai bằng IQR
quantity = df["Quantity"].dropna()

Q1 = quantity.quantile(0.25)
Q3 = quantity.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

mask = (df["Quantity"] < lower) | (df["Quantity"] > upper)

print("Q1:", Q1, "Q3:", Q3, "IQR:", IQR)
print("Ngưỡng dưới:", lower, "Ngưỡng trên:", upper)
print(df.loc[mask, ["OrderID", "Quantity"]])

# Bước 6. Quyết định xử lý và tạo dữ liệu sạch
clean_df = df.dropna(
    subset=["Quantity", "UnitPrice"]
).copy()

clean_df = clean_df[
    (clean_df["Quantity"] > 0) &
    (clean_df["UnitPrice"] > 0)
].copy()

print(clean_df.shape)

# Bước 7. Tính doanh thu và phân tích
clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"]

print("Tổng doanh thu:", clean_df["Revenue"].sum())

by_product = (
    clean_df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(by_product)

by_city = (
    clean_df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(by_city)

# Bước 8. Mã hóa dữ liệu phân loại
# 8.1. One-Hot Encoding
encoded_df = pd.get_dummies(
    clean_df,
    columns=["Category", "City"],
    dtype=int
)
print(encoded_df.head())

# 8.2. Ánh xạ nhãn có thứ tự
priority_map = {"Low": 1, "Medium": 2, "High": 3}
# Nếu có cột Priority:
# df["PriorityCode"] = df["Priority"].map(priority_map)

# Bước 9. Xuất CSV và Excel
clean_df.to_csv(
    "sales_clean.csv",
    index=False,
    encoding="utf-8-sig"
)

with pd.ExcelWriter("sales_report.xlsx", engine="openpyxl") as writer:
    clean_df.to_excel(writer, sheet_name="CleanData", index=False)
    by_product.to_frame("Revenue").to_excel(writer, sheet_name="ByProduct")
    by_city.to_frame("Revenue").to_excel(writer, sheet_name="ByCity")
