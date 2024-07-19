from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def add_grade(self, enrollment, grade):
        if enrollment in self._enrollments:
            self._grades[enrollment] = grade
        else:
            raise ValueError("The enrollment does not exist for this student")

    def aggregate_average_grade(self):
        if not self._grades:
            return None  # or raise an exception
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses

    def course_count(self):
        return len(self._enrollments)

class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            if date in enrollment_count:
                enrollment_count[date] += 1
            else:
                enrollment_count[date] = 1
        return enrollment_count
