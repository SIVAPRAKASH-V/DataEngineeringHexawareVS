from util.DBConnUtil import DBConnection


class Student(DBConnection):
    def __init__(self):
        super().__init__()
        self.studID = 0
        self.name = ''
        self.phNumber = ''

    # SETTERS
    def set_studID(self, value):
        self.studID = value

    def set_name(self, value):
        self.name = value

    def set_phNumber(self, value):
        self.phNumber = value

    # GETTERS
    def get_studID(self):
        return self.studID

    def get_name(self):
        return self.name

    def get_phNumber(self):
        return self.phNumber

    def __str__(self):
        return f'Student ID: {self.studID} Name: {self.name}\n' \
               f'Contact Number: {self.phNumber} '
