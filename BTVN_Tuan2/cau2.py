
import os

ten_nguon = input("Nhap ten tap tin nguon: ")
ten_dich = input("Nhap ten tap tin dich: ")

if os.path.exists(ten_nguon):
    print("Tap tin nguon da ton tai")

    f = open(ten_nguon, "r", encoding="utf-8")
    noi_dung = f.read()
    f.close()

    noi_dung = noi_dung.upper()

    f = open(ten_dich, "w", encoding="utf-8")
    f.write(noi_dung)
    f.close()