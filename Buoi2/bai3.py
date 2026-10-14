f = open("input3.txt", "r")

a, b = map(int, f.read().split())

f.close()

max_num = max(a, b)

f = open("output3.txt", "w", encoding="utf-8")
f.write(str(max_num))
f.close()