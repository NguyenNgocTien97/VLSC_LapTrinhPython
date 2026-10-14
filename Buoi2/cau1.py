f = open("numbers.txt", "r", encoding="utf-8")

ds = list(map(int, f.read().split()))

f.close()

tong = sum(ds)

f = open("output1.txt", "w")
f.write(str(tong) + "\n")
f.close()