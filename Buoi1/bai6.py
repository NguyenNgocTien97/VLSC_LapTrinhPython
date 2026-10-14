def count_enven(numbers):
    even = 0
    for number in numbers:
        if number % 2 == 0:
            even += 1
    return even

# lời gọi hàm
print(count_enven([10, 15, 22, 31, 40, 55]))