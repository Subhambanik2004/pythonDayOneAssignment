students = {}


def add_student(roll, name, cls):
    students[roll] = {"name": name, "class": cls}


def get_student(roll):
    return students.get(roll, "Student not found")


def display_students():
    for roll, data in students.items():
        print(roll, data)
