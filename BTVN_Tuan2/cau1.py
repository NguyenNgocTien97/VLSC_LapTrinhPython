
import os
import datetime

ten_file = input("Nhap ten tap tin: ")

if os.path.exists(ten_file):
    print("Tap tin da ton tai")

    kich_thuoc = os.path.getsize(ten_file)
    ngay_tao = os.path.getctime(ten_file)
    ngay_sua = os.path.getmtime(ten_file)

    print("Kich thuoc:", kich_thuoc, "byte")
    print("Ngay tao:", datetime.datetime.fromtimestamp(ngay_tao))
    print("Ngay sua:", datetime.datetime.fromtimestamp(ngay_sua))

    f = open(ten_file, "r", encoding="utf-8")
    noi_dung = f.read().strip()
    f.close()

    print("Noi dung tap tin:", noi_dung)

else:
    print("Tap tin khong ton tai")
