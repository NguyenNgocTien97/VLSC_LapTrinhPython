f = open("input5.txt", "r")

n = int(f.readline().strip())

diem_dong = f.readline().strip()

diem = list(map(int, diem_dong.split()))
f.close()

diem_cao_nhat = max(diem)

f = open("output5.txt", "w", encoding="utf-8")
f.write(str(diem_cao_nhat) + "\n")
f.close()
