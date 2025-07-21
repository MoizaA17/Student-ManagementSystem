from student import Student
from course import Course
import os
import json

def student_exists(students_list):
    id = input("Enter student's ID: ")
    
    for student in students_list:
        if student.id == id:
            return student
    
    return None

def student_exist(students_list):
    id = input("Enter student's ID: ")
    
    for student in students_list:
        if student.id == id:
            return student, student.id
    
    return None, id
    
def add_a_student(students_list):
    student, id = student_exist(students_list)

    if(student):
        print ("\nStudent already exists with this id: ", id)
            
        
    else:
        name = input("Enter Students's Name: ")
        age = input("Enter Students's Age: ")
        while True:
            contact = input("Enter Students's Contact number (without dashes): ")
            if len(contact) == 11:
                student = Student(name,id,age,contact)
                students_list.append(student)
                print ("\nNew student added Successfully.")
                break

            else:
                print("Enter correct Contact number. ")


def display_all_students(students_list):
    print("\nTotal students are: ", len(students_list), "\n")
    for student in students_list:
        student.display_info()
        print("\n")

def Search_student_by_ID(students_list):
    student = student_exists(students_list)
    if(student):
        student.display_info()

    else:
        print("Student does not exist.")
           
            

def update_info(students_list):
    student = student_exists(students_list)
    if(student):
        student.update_info()
        print("\nStudent info updated successfully.")

    else:
        print("Student does not exist.")


    

def delete_student(students_list):
    student = student_exists(students_list)
    if(student):
        students_list.remove(student)
        print("\nThe student is deleted successfully.")

    else:
        print("Student does not exist.")

def enroll_in_a_course(students_list):
   student = student_exists(students_list)
   if(student):
        course_code = input("Enter Course Code: ")
        print(student.add_course(course_code))

   else:
       print("\nStudent does not exist.")


def remove_course(students_list):
   student = student_exists(students_list)
   if(student):
    course_code = input("Enter course code to remove student from: ").lower().strip()
    print(student.remove_course(course_code))

   else:
       print("\nStudent does not exist.")


def save_students(filename, students_list):
    student_dict = []
    for student in students_list:
        student_dict.append(student.to_dict())

    with open(filename, "w") as file:
        json.dump(student_dict, file, indent = 4)

        print("students saved successfully.")


def load_students(filename):

    if os.path.exists(filename):
        with open(filename, "r") as file:
            data =  json.load(file)
            print("Data is loaded.")
            return data
        
    else:
        return []
    

def main():
    students_list = []
    try:
        filename = "students.json"
        loadedData =  load_students(filename)
        if(loadedData == []):
            pass
        else:
            for student_dic in loadedData:
                course_obj = [Course(course["course_name"],course["course_code"],course["instructor"],course["credit_hours"]) for course in student_dic["courses"]]
                student_dic["courses"] = course_obj
                student = Student(**student_dic)
                students_list.append(student)

    except:
        print("I am error")
        
    while True:
    # try:
        print("----------Main Menu-------------")
        print("\nEnter 1 to add a Student.\nEnter 2 to display all Students.\nEnter 3 to search student by ID.\nEnter 4 to update student info. \nEnter 5 to delete a Student. \nEnter 6 to enroll a student in a Course.\nEnter 7 to remove a student from a Course. \nEnter 8 to Exit. \n")
        choice = int(input("Enter your choice: "))

        if(choice == 1):
            add_a_student(students_list)

        elif(choice == 2):
            display_all_students(students_list)

        elif(choice == 3):
            Search_student_by_ID(students_list)

        elif(choice == 4):
            update_info(students_list)

        elif(choice == 5):
            delete_student(students_list)

        elif(choice == 6):
            enroll_in_a_course(students_list)

        elif(choice == 7):
            remove_course(students_list)


        elif(choice == 8):
            save_students(filename, students_list)
            break

        else: 
            print("Not a valid option")

    # except:
    #     print("Only integer number is served.")

main()