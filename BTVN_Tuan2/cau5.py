
f = open("data5.txt", "a", encoding="utf-8")

while True:
    noi_dung = input("Nhap noi dung (nhap exit de dung): ")

    if noi_dung == "exit":
        break
    else:
        f.write(noi_dung + "\n")

f.close()

