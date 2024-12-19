# app.py FULLY FUNCTIONAL
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment
from utils.exception_handling import CourseLimitExceededException, CourseNotFoundException

def school_officer_menu():
    """School officer menu to add, delete, or update student/course."""
    print("\n--- School Officer Menu ---")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Add Course")
    print("4. Delete Course")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        phone = input("Enter Phone Number: ")
        student = Student(student_id, name, phone)
        student.register()
        print("Student added successfully!")
    
    elif choice == '2':
        student_id = int(input("Enter Student ID to delete: "))
        student = Student(student_id)
        student.delete()
        print("Student deleted successfully!")  
    
    elif choice == '3':
        course_id = int(input("Enter Course ID: "))
        course_name = input("Enter Course Name: ")
        instructor = input("Enter Instructor Name: ")
        course = Course(course_id, course_name, instructor)
        course.add_course()
        print("Course added successfully!")
    
    elif choice == '4':
        course_id = int(input("Enter Course ID to delete: "))
        course = Course(course_id)
        course.delete() 
        print("Course deleted successfully!")  
    
    elif choice == '5':
        return
    
    else:
        print("Invalid choice. Please try again.")
    school_officer_menu()

def student_menu():
    """Student menu to register or deregister for courses."""
    print("\n--- Student Menu ---")
    print("0. View Available Course")
    print("1. Register for Course")
    print("2. Deregister from Course")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        student_id = int(input("Enter Student ID: "))
        course_id = int(input("Enter Course ID to register: "))
        enrollment = Enrollment(student_id, course_id)
        try:
            enrollment.register_course()
            print("Course registered successfully!")
        except CourseLimitExceededException as cle:
            print(f"Error: {cle}")
        except CourseNotFoundException as cnf:
            print(f"Error: {cnf}")
    
    elif choice == '2':
        student_id = int(input("Enter Student ID: "))
        course_id = int(input("Enter Course ID to deregister: "))
        enrollment = Enrollment(student_id, course_id)
        enrollment.deregister_course()
        print("Course deregistered successfully!")
    elif choice == '0':
        Course.display_all_courses()

    elif choice == '3':
        return
    
    else:
        print("Invalid choice. Please try again.")
    student_menu()

def main_menu():
    """Main menu to select user type."""
    while True:
        print("\n--- Main Menu ---")
        print("1. School Officer")
        print("2. Student")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            school_officer_menu()
        
        elif choice == '2':
            student_menu()
        
        elif choice == '3':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
