# models/student.py
from config import get_db_connection

class Student:
    def __init__(self, student_id, name = None, phone=None):
        self.student_id = student_id
        self.name = name
        self.phone = phone
    
    def register(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO student (StudentID, Name, PhoneNumber) VALUES (?, ?, ?)", 
                (self.student_id, self.name, self.phone)
            )
            conn.commit()
        except Exception as e:
            print(f"Error registering student: {e}")
        finally:
            conn.close()

    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Students WHERE StudentID = ?", (self.student_id,))
            conn.commit()
        except Exception as e:
            print(f"Error deleting student: {e}")
        finally:
            conn.close()
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM student WHERE StudentID = ?", (self.student_id,))
            student = cursor.fetchone()
            
            if not student:
                print(f"Student with ID {self.student_id} does not exist.")
                return
            
            cursor.execute("DELETE FROM student WHERE StudentID = ?", (self.student_id,))
            conn.commit()
            print(f"Student with ID {self.student_id} deleted successfully.")
        
        except Exception as e:
            print(f"Error deleting student: {e}")
        finally:
            conn.close()
    