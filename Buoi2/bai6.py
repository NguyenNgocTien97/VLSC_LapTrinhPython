f = open("input6.txt", "r") 

noi_dung = f.read().strip()
diem = list(map(int, noi_dung.split()))

diem_cao_nhat = max(diem)

f = open("output6.txt", "w", encoding="utf-8")
f.write(str(diem_cao_nhat) + "\n")
f.close()
