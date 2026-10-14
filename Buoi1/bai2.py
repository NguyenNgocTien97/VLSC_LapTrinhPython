# # khai báo và  khởi tạo hàm
# def check_number(n):
#     if n % 2 == 0:
#         return "even"
#     return "odd"

# def check_number_2(n):
#    return n % 2 == 0 if "even" else "odd"

# hàm lambda
is_check = lambda x : "Even" if x % 2 == 0 else "Odd"
# lời gọi hàm
print(is_check(10))  
print(is_check(9))