# models/course.py
from config import get_db_connection

class Course:
    def __init__(self, course_id, course_name=None, instructor=None):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor

    def add_course(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO course (CourseID, CourseName, instructor) VALUES (?, ?, ?)", 
                (self.course_id, self.course_name, self.instructor)
            )
            conn.commit()
        except Exception as e:
            print(f"Error adding course: {e}")
        finally:
            conn.close()
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM course WHERE CourseID = ?", (self.course_id,))
            course = cursor.fetchone()
            
            if not course:
                print(f"Course with ID {self.course_id} does not exist.")
                return
            
            cursor.execute("DELETE FROM course WHERE CourseID = ?", (self.course_id,))
            conn.commit()
            print(f"Course with ID {self.course_id} deleted successfully.")
        
        except Exception as e:
            print(f"Error deleting course: {e}")
        finally:
            conn.close()
    

    @staticmethod
    def display_all_courses():
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT CourseID, CourseName, instructor FROM Course")
            courses = cursor.fetchall()
            
            if not courses:
                print("No courses available.")
                return
            
            print("\n--- Available Courses ---")
            for course in courses:
                print(f"Course ID: {course[0]}, Course Name: {course[1]}, Instructor: {course[2]}")
        
        except Exception as e:
            print(f"Error displaying courses: {e}")
        finally:
            conn.close()
