def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# lời gọi hàm
print(get_grade(90))
print(get_grade(80))
print(get_grade(70))
print(get_grade(60))
print(get_grade(50))