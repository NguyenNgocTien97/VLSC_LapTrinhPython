ho_ten = input("Ho va ten: ")
tuoi = input("Nhap tuoi: ")

f = open("data2.txt", "w", encoding="utf-8")
f.write("Ho va ten: " + ho_ten + "\n")
f.write("Tuoi: " + tuoi + "\n")