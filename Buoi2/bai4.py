f = open("input4.txt", "r")

hoten = f.readline().strip()
toan, ly, hoa = map(float, f.readline().split())

f.close()

dtb = (toan + ly + hoa) / 3

if dtb >= 8:
    xeploai = "Gioi"
elif dtb >= 6.5:
    xeploai = "Kha"
elif dtb >= 5:
    xeploai = "Trung binh"
else:
    xeploai = "Yeu"

f = open("output4.txt", "w", encoding="utf-8")

f.write(hoten + "\n")
f.write("Diem trung binh: " + str(round(dtb, 2)) + "\n")
f.write("Xep Loai: " + xeploai)

f.close()