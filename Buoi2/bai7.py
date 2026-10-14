f = open("input7.txt", "r", encoding="utf-8")
n = int(f.readline().strip())
so_dong = f.readline().strip()
day_so = list(map(int, so_dong.split()))
f.close()
day_so.sort()

ket_qua = " ".join(map(str, day_so))

f = open("output7.txt", "w", encoding="utf-8")
f.write(ket_qua + "\n")
f.close()
