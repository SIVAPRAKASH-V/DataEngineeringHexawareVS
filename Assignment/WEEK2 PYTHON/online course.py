class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.enrolled_courses = []

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)
            print(f"{self.username} has enrolled in '{course.title}'.")
        else:
            print(f"{self.username} is already enrolled in '{course.title}'.")

class Course:
    def __init__(self, title, description, instructor):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.students = []
        self.materials = []
        self.assignments = {}

    def add_student(self, student):
        self.students.append(student)

    def add_material(self, material):
        self.materials.append(material)

    def add_assignment(self, assignment_title):
        self.assignments[assignment_title] = {}

    def submit_assignment(self, assignment_title, student, submission):
        if assignment_title in self.assignments:
            self.assignments[assignment_title][student] = {"submission": submission, "feedback": None}
            print(f"{student.username} submitted '{assignment_title}'.")
        else:
            print(f"Assignment '{assignment_title}' does not exist in this course.")

    def provide_feedback(self, assignment_title, student, feedback):
        if assignment_title in self.assignments and student in self.assignments[assignment_title]:
            self.assignments[assignment_title][student]["feedback"] = feedback
            print(f"Feedback for '{assignment_title}' provided to {student.username}.")
        else:
            print(f"No submission found for '{assignment_title}' by {student.username}.")

class OnlineLearningPlatform:
    def __init__(self):
        self.users = {}
        self.courses = {}

    def register_user(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        if username in self.users:
            print("User already exists!")
            return
        user = User(username, email)
        self.users[username] = user
        print(f"User '{username}' registered successfully.")

    def create_course(self):
        title = input("Enter course title: ")
        description = input("Enter course description: ")
        instructor = input("Enter instructor name: ")
        if title in self.courses:
            print("Course already exists!")
            return
        course = Course(title, description, instructor)
        self.courses[title] = course
        print(f"Course '{title}' created successfully.")

    def enroll_in_course(self):
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found. Please register first.")
            return
        user = self.users[username]
        course_title = input("Enter the course title you want to enroll in: ")
        if course_title not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_title]
        user.enroll(course)

    def view_courses(self):
        if not self.courses:
            print("No courses available at the moment.")
        else:
            for title, course in self.courses.items():
                print(f"Title: {course.title}, Description: {course.description}, Instructor: {course.instructor}")

    def access_course_materials(self):
        course_title = input("Enter the course title: ")
        if course_title not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_title]
        print(f"Materials for '{course.title}':")
        if not course.materials:
            print("No materials available.")
        else:
            for material in course.materials:
                print(material)

    def submit_assignment(self):
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found. Please register first.")
            return
        user = self.users[username]
        course_title = input("Enter the course title: ")
        if course_title not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_title]
        assignment_title = input("Enter the assignment title: ")
        submission = input("Enter your assignment submission: ")
        course.submit_assignment(assignment_title, user, submission)

    def provide_feedback(self):
        course_title = input("Enter the course title: ")
        if course_title not in self.courses:
            print("Course not found.")
            return
        course = self.courses[course_title]
        assignment_title = input("Enter the assignment title: ")
        username = input("Enter the student's username: ")
        if username not in self.users:
            print("Student not found.")
            return
        student = self.users[username]
        feedback = input("Enter feedback: ")
        course.provide_feedback(assignment_title, student, feedback)

    def menu(self):
        while True:
            print("\nOnline Learning Platform")
            print("1. Register User")
            print("2. Create Course")
            print("3. Enroll in Course")
            print("4. View Courses")
            print("5. Access Course Materials")
            print("6. Submit Assignment")
            print("7. Provide Feedback")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.create_course()
            elif choice == "3":
                self.enroll_in_course()
            elif choice == "4":
                self.view_courses()
            elif choice == "5":
                self.access_course_materials()
            elif choice == "6":
                self.submit_assignment()
            elif choice == "7":
                self.provide_feedback()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    platform = OnlineLearningPlatform()
    platform.menu()
