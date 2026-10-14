import os

ten_file = input("Nhap ten tap tin: ")

if os.path.exists(ten_file):
    print("Tap tin da ton tai")
    f = open(ten_file, "r", encoding="utf-8")
    noi_dung = f.read()
    f.close()

    so_dong = len(noi_dung.splitlines())
    so_tu = len(noi_dung.split())
    so_ky_tu = len(noi_dung.replace(" ", "").replace("\n", "").replace("\t", ""))

    print("so dong: ", so_dong)
    print("so tu: ", so_tu)
    print("so ky tu: ", so_ky_tu)

else:
    print("Tap tin khong ton tai")
