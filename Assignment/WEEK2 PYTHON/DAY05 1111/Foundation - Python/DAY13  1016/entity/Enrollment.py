from entity.Course import Course
from entity.Student import Student


class Enrollment(Course, Student):
    def __init__(self):
        super().__init__()
        self.enrollID = 0
        self.studID = 0
        self.courseID = 0

    # SETTERS
    def set_enrollID(self, value):
        self.enrollID = value

    def set_studID(self, value):
        self.studID = value

    def set_courseID(self, value):
        self.courseID = value

    # GETTERS
    def get_enrollID(self):
        return self.enrollID

    def get_studID(self):
        return self.studID

    def get_courseID(self):
        return self.courseID

    def __str__(self):
        return f'Enrollment ID ID: {self.enrollID}\n' \
               f'Student ID: {self.studID} Course ID: {self.courseID}'
