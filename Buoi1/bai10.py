def analyze_numbers(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even = 0
    odd = 0

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total += num
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    average = total / len(numbers)

    print("Largest number:", largest)
    print("Smallest number:", smallest)
    print("Sum:", total)
    print(f"Average: {average:.2f}")
    print("Even numbers:", even)
    print("Odd numbers:", odd)

analyze_numbers([12, 5, 8, 21, 30, 17, 4])