from course import Course

class Student:
    def __init__(self, name, id, age, contact, courses = None):
        self.name = name
        self.id = id
        self.age = age
        self.contact = contact
        self.courses = courses if courses else []

    def add_course(self, course_code):
        course_exist = False

        for course in self.courses:
            if course.course_code == course_code:
                course_exist = True
                return ("\nStudent is already enrolled in this course.")
            
        if(course_exist!=True):
            course_name = input("Enter Course Name: ")
            instructor = input("Enter Instructor Name: ")
            credit_hours = input("Enter Course Credit Hours: ")

            course = Course(course_name, course_code, instructor, credit_hours)
            self.courses.append(course)

            return ("\nStudent enrolled in the course Successfully.")


    def remove_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                self.courses.remove(course)
                return "\nStudent removed from a course successfully."

        return "Student is not enrolled in this course."

    def update_info(self):
        answer = input("What do you want to update (name/age/contact): ").lower().strip()

        if(answer == "name"):
            new_name = input("Enter Updated Name: ").strip()
            self.name = new_name
            print("\nName updated successfully.")


        elif(answer == "age"):

            try: 
                new_age = int(input("Enter Updated Age: ").strip())
                self.age = new_age
                print("\nAge updated successfully.")

            except:
                print("Enter valid age.")

        elif(answer == "contact"):
            try:
                new_contact = int(input("Enter updated Contact number (without dashes): "))
                if(len(new_contact) == 11):
                    self.contact = new_contact
                    print("\nContact updated successfully.")

            except:
                print("Enter valid contact.")

        else:
            print("Enter valid option.")

    def get_CourseName(self):
        course_list = []
        for course in self.courses:
            course_list.append(course.course_name)
        
        return course_list
    
    def display_info(self):
        print(f"Student Name: {self.name} \nStudent ID: {self.id} \nStudent Age: {self.age} \nStudent Contact {self.contact} \nCourses enrolled: {self.get_CourseName()}" )
        
        
    def course_info(self):
        for course in self.courses:
            course.display_info()

    def to_dict(self):
        return {
            "name" : self.name,
            "id" : self.id,
            "age"  : self.age,
            "contact" : self.contact,
            "courses" : [course.to_dict() for course in self.courses]

        }