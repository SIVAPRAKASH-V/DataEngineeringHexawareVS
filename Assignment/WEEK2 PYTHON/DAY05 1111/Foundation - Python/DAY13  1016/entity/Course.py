from util.DBConnUtil import DBConnection


class Course(DBConnection):
    def __init__(self):
        super().__init__()
        self.CourseID = 0
        self.courseName = ''
        self.instructor = ''

    # SETTERS
    def set_courseID(self, value):
        self.courseID = value

    def set_courseName(self, value):
        self.courseName = value

    def set_instructor(self, value):
        self.instructor = value


    # GETTERS
    def get_courseID(self):
        return self.courseID

    def get_courseName(self):
        return self.courseName

    def get_instructor(self):
        return self.instructor

    def __str__(self):
        return f'Course ID: {self.courseID} Course Name: {self.courseName}\n' \
               f'Instructor: {self.instructor}' 
