class Student:
    count = 0
    def __init__(self):
        self.count += 1

    def getTotalStudents(self):
        return self.count