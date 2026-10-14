f = open("numbers.txt", "r")

ds = list(map(int, f.read().split()))

f.close()

lon_nhat = max(ds)
nho_nhat = min(ds)

f = open("output2.txt", "w", encoding="utf-8")

f.write("So lon nhat: " + str(lon_nhat) + "\n")
f.write("So nho nhat: " + str(nho_nhat))

f.close()