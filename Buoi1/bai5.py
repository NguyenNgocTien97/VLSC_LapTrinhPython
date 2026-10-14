def calculate_sum(n):
    if n == 1:
        return 1
    else:
        return n + calculate_sum(n - 1)

# lời gọi hàm
print(calculate_sum(10))
        