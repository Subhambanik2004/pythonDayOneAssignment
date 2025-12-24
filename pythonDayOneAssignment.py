students = {
    "Amit": [85, 90, 88],
    "Riya": [92, 95, 91],
    "Karan": [70, 65, 68],
    "Sneha": [78, 80, 75],
    "Neha": [55, 58, 60],
}


def calculate_average(marks):
    return sum(marks) / len(marks)


# Variables to track top scorer
top_student = ""
top_average = 0


print("Student Result:\n")

for name, marks in students.items():
    average = calculate_average(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print("Name:", name)
    print("Average Marks:", average)
    print("Grade:", grade)
    print("-------------------")

    if average > top_average:
        top_average = average
        top_student = name


print(" Top Scorer ")
print("Name:", top_student)
print("Average Marks:", top_average)
