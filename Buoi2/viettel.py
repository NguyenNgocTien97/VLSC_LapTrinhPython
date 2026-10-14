f = open("viettel_data.txt", "r", encoding="utf-8")
data = f.read()
data = data.split(",")
get_data = data[len(data) - 1]
total = int(get_data) * 1000
print(total)
f.close()