# khai báo và định nghĩa hàm
def find_max(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

# lời gọi hàm
print(find_max(28, 15, 20))