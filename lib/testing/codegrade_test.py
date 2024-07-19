import pytest
from datetime import datetime
from lib.enrollment import Student, Course, Enrollment

def test_aggregate_methods():
    student1 = Student("John")
    student2 = Student("Jane")
    
    course1 = Course("Math")
    course2 = Course("Science")
    
    student1.enroll(course1)
    enrollment2 = student1.enroll(course2)
    enrollment3 = student2.enroll(course1)
    
    student1.add_grade(student1.get_enrollments()[0], 90)
    student1.add_grade(student1.get_enrollments()[1], 80)
    
    assert student1.course_count() == 2
    assert student2.course_count() == 1
    
    enrollments_per_day = Enrollment.aggregate_enrollments_per_day()
    assert len(enrollments_per_day) == 1  # assuming all enrollments happened on the same day
    assert enrollments_per_day[list(enrollments_per_day.keys())[0]] == 3
    
    assert student1.aggregate_average_grade() == 85
    assert student2.aggregate_average_grade() is None

class TestCodegrade:
    '''Codegrade placeholder'''

    def test_codegrade_placeholder(self):
        assert(True)
