def find_passed_students(students):
    for key, value in students.items():
        if value >= 5:
            print(key, value)

# lời gọi hàm
find_passed_students({"DarkTim": 8, "Khoa Bug": 6, "Adui": 10, "Tubeo": 4})