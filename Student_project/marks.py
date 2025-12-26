marks_data = {}


def add_marks(roll, marks):
    marks_data[roll] = marks


def calculate_average(roll):
    return sum(marks_data[roll]) / len(marks_data[roll])
