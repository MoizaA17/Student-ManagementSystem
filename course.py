class Course:
    def __init__(self, course_name, course_code, instructor, credit_hours):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.credit_hours = credit_hours

    def display_info(self):
        print(f"Course Name {self.course_name}, \nCourse Code: {self.course_code}, \nCourse Instructor: {self.instructor}, \nCredit Hours: {self.credit_hours} \n\n")

    def to_dict(self):
        return {
            "course_name" : self.course_name,
            "course_code" : self.course_code,
            "instructor"  : self.instructor,
            "credit_hours" : self.credit_hours
        }