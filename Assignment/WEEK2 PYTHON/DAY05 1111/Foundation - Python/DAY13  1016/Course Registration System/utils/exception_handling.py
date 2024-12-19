# utils/exception_handling.py

class CourseLimitExceededException(Exception):
    """Exception raised when student exceeds course limit."""
    pass

class CourseNotFoundException(Exception):
    """Exception raised when course is not found."""
    pass
