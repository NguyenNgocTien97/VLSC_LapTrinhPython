import pandas as pd
import numpy as np

df = pd.read_csv(r"d:\DataMining\Buoi5\sales_practice_dataset.csv", encoding="utf-8-sig")

# ============================================================
# Bài 1. Khám phá dữ liệu
# ============================================================

# 10. Đọc file, hiển thị 5 dòng đầu và 5 dòng cuối.
print("=== 10. 5 dòng đầu ===")
print(df.head())
print("\n=== 10. 5 dòng cuối ===")
print(df.tail())

# 11. Cho biết số dòng, số cột, tên cột và kiểu dữ liệu.
print("\n=== 11. Số dòng, số cột ===")
print("Shape:", df.shape)
print("\nTên cột:", df.columns.tolist())
print("\nKiểu dữ liệu:")
print(df.dtypes)

# 12. Thống kê số giá trị thiếu theo từng cột.
print("\n=== 12. Giá trị thiếu theo từng cột ===")
print(df.isna().sum())

# 13. Liệt kê sản phẩm, nhóm hàng và thành phố khác nhau.
print("\n=== 13. Các giá trị khác nhau ===")
print("Sản phẩm:", df["Product"].unique())
print("Nhóm hàng:", df["Category"].unique())
print("Thành phố:", df["City"].unique())

# ============================================================
# Bài 2. Làm sạch dữ liệu
# ============================================================

# 14. Chuẩn hóa Product, Category và City.
print("\n=== 14. Chuẩn hóa văn bản ===")
df["Product"] = df["Product"].str.strip()
df["Category"] = df["Category"].str.strip()
df["City"] = df["City"].str.strip()
print("Sau chuẩn hóa - City:", df["City"].unique())

# 15. Tìm các dòng thiếu Quantity hoặc UnitPrice.
print("\n=== 15. Dòng thiếu Quantity hoặc UnitPrice ===")
missing = df[df["Quantity"].isna() | df["UnitPrice"].isna()]
print(missing)

# 16. Tìm Quantity <= 0 và UnitPrice <= 0.
print("\n=== 16. Quantity <= 0 ===")
print(df[df["Quantity"] <= 0])
print("\n=== 16. UnitPrice <= 0 ===")
print(df[df["UnitPrice"] <= 0])

# 17. Đề xuất cách xử lý từng trường hợp và giải thích.
# - Thiếu Quantity hoặc UnitPrice: LOẠI BỎ vì không thể tính doanh thu,
#   không nên điền 0 vì sẽ làm sai tổng doanh thu.
# - Quantity <= 0: LOẠI BỎ vì vi phạm quy tắc nghiệp vụ (số lượng âm vô nghĩa).
# - UnitPrice <= 0: LOẠI BỎ vì đơn giá không thể âm hoặc bằng 0.
# - Quantity rất lớn (vd: 150): GIỮ LẠI để xác minh, có thể là đơn hàng lớn hợp lệ.
print("\n=== 17. Đề xuất xử lý ===")
print("- Thiếu Quantity/UnitPrice => loại bỏ (không thể tính doanh thu)")
print("- Quantity <= 0            => loại bỏ (vi phạm nghiệp vụ)")
print("- UnitPrice <= 0           => loại bỏ (đơn giá không hợp lệ)")
print("- Quantity lớn bất thường  => giữ lại, cần xác minh chứng từ")

# 18. Tạo clean_df, không ghi đè dữ liệu gốc.
print("\n=== 18. Tạo clean_df ===")
clean_df = df.dropna(subset=["Quantity", "UnitPrice"]).copy()
clean_df = clean_df[
    (clean_df["Quantity"] > 0) &
    (clean_df["UnitPrice"] > 0)
].copy()
print("Shape clean_df:", clean_df.shape)
print("Shape df gốc:", df.shape, "(không thay đổi)")

# ============================================================
# Bài 3. Phân tích ngoại lai
# ============================================================

# 19. Tính Q1, Q3, IQR và hai ngưỡng cho Quantity.
print("\n=== 19. IQR Quantity ===")
quantity = df["Quantity"].dropna()
Q1 = quantity.quantile(0.25)
Q3 = quantity.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(f"Q1={Q1}  Q3={Q3}  IQR={IQR}")
print(f"Ngưỡng dưới={lower}  Ngưỡng trên={upper}")

# 20. Liệt kê OrderID bị đánh dấu ngoại lai.
print("\n=== 20. OrderID ngoại lai ===")
mask = (df["Quantity"] < lower) | (df["Quantity"] > upper)
print(df.loc[mask, ["OrderID", "Quantity"]])

# 21. So sánh kết quả khi giữ và khi loại giá trị ngoại lai.
print("\n=== 21. So sánh giữ / loại ngoại lai ===")
kept = clean_df["Quantity"].describe()
without_outlier = clean_df[
    ~((clean_df["Quantity"] < lower) | (clean_df["Quantity"] > upper))
]["Quantity"].describe()
compare = pd.DataFrame({"Giữ ngoại lai": kept, "Loại ngoại lai": without_outlier})
print(compare)

# 22. Giải thích vì sao ngoại lai không đồng nghĩa với dữ liệu sai.
# Ngoại lai là giá trị nằm ngoài ngưỡng IQR, không có nghĩa là sai.
# Ví dụ: Quantity=150 có thể là đơn hàng lớn hợp lệ (công ty, sự kiện).
# Cần kiểm tra chứng từ/bối cảnh nghiệp vụ trước khi quyết định loại bỏ.
print("\n=== 22. Giải thích ngoại lai ===")
print("Ngoại lai chỉ là giá trị bất thường về mặt thống kê, không chắc là sai.")
print("Quantity=150 có thể là đơn hàng lớn hợp lệ => cần xác minh, không tự xóa.")

# ============================================================
# Bài 4. Mã hóa dữ liệu
# ============================================================

# 23. Mã hóa Category bằng pd.get_dummies().
print("\n=== 23. One-Hot Encoding Category ===")
encoded_category = pd.get_dummies(clean_df, columns=["Category"], dtype=int)
cat_cols = ["OrderID"] + [c for c in encoded_category.columns if c.startswith("Category")]
print(encoded_category[cat_cols].head())

# 24. Mã hóa City bằng pd.get_dummies().
print("\n=== 24. One-Hot Encoding City ===")
encoded_df = pd.get_dummies(clean_df, columns=["Category", "City"], dtype=int)

# 25. In 5 dòng sau mã hóa và giải thích các cột 0/1.
print("\n=== 25. 5 dòng sau mã hóa (Category + City) ===")
print(encoded_df.head())
# Giải thích: mỗi nhãn tạo 1 cột nhị phân.
# Dòng thuộc nhóm đó = 1, các nhóm khác = 0.
# Ví dụ: Category_Electronics=1 => sản phẩm thuộc Electronics.
print("\nGiải thích: mỗi nhãn tạo 1 cột; thuộc nhóm = 1, còn lại = 0.")

# 26. Giải thích vì sao không nên gán thứ tự số tùy ý cho Category.
# Category là biến danh nghĩa (nominal), không có thứ tự tự nhiên.
# Nếu gán Accessories=1, Electronics=2 => mô hình sẽ hiểu Electronics > Accessories,
# dẫn đến sai lệch trong kết quả học máy.
print("\n=== 26. Không nên gán số tùy ý cho Category ===")
print("Category không có thứ tự => gán số tạo ra quan hệ thứ tự giả.")
print("=> Dùng One-Hot Encoding để biểu diễn trung lập, không gây sai lệch.")

# ============================================================
# Bài 5. Phân tích doanh thu
# ============================================================

# 27. Tạo Revenue = Quantity * UnitPrice.
print("\n=== 27. Tạo cột Revenue ===")
clean_df["Revenue"] = clean_df["Quantity"] * clean_df["UnitPrice"]
print(clean_df[["OrderID", "Quantity", "UnitPrice", "Revenue"]].head())

# 28. Tính tổng doanh thu trên dữ liệu đã làm sạch.
print("\n=== 28. Tổng doanh thu ===")
print(f"Tổng doanh thu: {clean_df['Revenue'].sum():,.0f} VNĐ")

# 29. Tính doanh thu theo Product và sắp xếp giảm dần.
print("\n=== 29. Doanh thu theo Product (giảm dần) ===")
by_product = (
    clean_df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(by_product)

# 30. Tính doanh thu theo City.
print("\n=== 30. Doanh thu theo City (giảm dần) ===")
by_city = (
    clean_df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(by_city)

# 31. Tìm sản phẩm và thành phố có doanh thu cao nhất.
print("\n=== 31. Doanh thu cao nhất ===")
print(f"Sản phẩm: {by_product.idxmax()} ({by_product.max():,.0f} VNĐ)")
print(f"Thành phố: {by_city.idxmax()} ({by_city.max():,.0f} VNĐ)")

# 32. Viết 3–5 nhận xét dựa trên kết quả.
print("\n=== 32. Nhận xét ===")
print("1. Webcam và Laptop dẫn đầu doanh thu dù số đơn hàng không nhiều,")
print("   nguyên nhân do đơn giá cao hoặc số lượng mua lớn.")
print("2. Hanoi có doanh thu cao nhất, cho thấy thị trường phía Bắc tiêu thụ mạnh.")
print("3. Wireless Mouse và USB Drive có doanh thu thấp nhất do đơn giá thấp.")
print("4. Can Tho đứng cuối về doanh thu, cần chiến lược phát triển thị trường.")
print("5. Sau làm sạch còn 17/20 dòng hợp lệ để tính doanh thu.")
