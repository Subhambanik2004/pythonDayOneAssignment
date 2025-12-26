class Report:
    def __init__(self, roll, name, avg, attendance):
        self.roll = roll
        self.name = name
        self.avg = avg
        self.attendance = attendance

    def generate(self):
        print("----- REPORT CARD -----")
        print("Roll:", self.roll)
        print("Name:", self.name)
        print("Average Marks:", self.avg)
        print("Attendance:", self.attendance, "%")
