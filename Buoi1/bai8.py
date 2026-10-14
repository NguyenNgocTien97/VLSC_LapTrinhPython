def display_student(student):
    for key, value in student.items():
        print(key, value)

# lời gọi hàm
display_student({"Name:": "Nguyễn Ngọc Tiến", "age:": 19, "major:": "CNTT", "score:": 8.5})