import math
import datetime
import random

print("Rounded Avg:", math.ceil(72.4))
print("Date:", datetime.date.today())
print("Random ID:", random.randint(1000, 9999))


import student
import attendance as att
from marks import add_marks, calculate_average
from report import Report
from utils import grade

student.add_student(1, "Rahul", "SE")
add_marks(1, [70, 80, 90])
att.mark_attendance(1, 92)

avg = calculate_average(1)
rep = Report(1, "Rahul", avg, 92)

rep.generate()
print("Grade:", grade(avg))
