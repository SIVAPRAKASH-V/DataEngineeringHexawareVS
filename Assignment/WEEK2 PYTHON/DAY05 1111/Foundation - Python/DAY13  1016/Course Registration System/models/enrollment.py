# models/enrollment.py
from config import get_db_connection
from utils.exception_handling import CourseLimitExceededException, CourseNotFoundException

class Enrollment:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    def register_course(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM course WHERE CourseID = ?", (self.course_id,))
            course = cursor.fetchone()
            if not course:
                raise CourseNotFoundException(f"Course with ID {self.course_id} does not exist.")

            cursor.execute("SELECT COUNT(*) FROM enrollments WHERE StudentID = ?", (self.student_id,))
            course_count = cursor.fetchone()[0]
            if course_count >= 5:
                raise CourseLimitExceededException("Students cannot enroll in more than 5 courses.")

            cursor.execute(
                "INSERT INTO enrollments (StudentID, CourseID) VALUES (?, ?)", 
                (self.student_id, self.course_id)
            )
            conn.commit()

            with open('logs/registration.log', 'a') as log_file:
                log_file.write(f"Student {self.student_id} registered for Course {self.course_id}\n")

        except Exception as e:
            print(f"Error during course registration: {e}")
        finally:
            conn.close()

    def deregister_course(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM enrollments WHERE StudentID = ? AND CourseID = ?", 
                           (self.student_id, self.course_id))
            conn.commit()

            with open('logs/registration.log', 'a') as log_file:
                log_file.write(f"Student {self.student_id} deregistered from Course {self.course_id}\n")
        except Exception as e:
            print(f"Error during course deregistration: {e}")
        finally:
            conn.close()
