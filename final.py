"""ITF 08 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Noor Abo Samra
Delivery Date : 31.8.2023
"""


# TODO 2 Define Course Class and define constructor with

# import  uuid
# class Course:
#     def __int__(self,course_name,course_mark):
#         self.course_id=uuid.uuid4()
#         self.course_name=course_name
#         self.course_mark=course_mark
# course_name=input('entre name ')
# course_mark=input('entre mark ')


#
# class Student:
#     # TODO 3 define static variable indicates total student count
# student_number=0
# def __init__(self):
#     print('instance created successfully')
#     Student.student_number+=1
# ob1=Student()
# ob2=Student()
# print(ob2.student_number)
# print(ob1.student_number)
# students=[]
#
#     # TODO 4 define a constructor which includes
# import uuid
#
#
# def __int__(self, name, age , number):
#     self.id = uuid.uuid4()
#     self.name = name
#     self.age=age
#     self.number=number
#     self.Course=[]
#
#     def add_course(self, course):
#         self.courses.append(course)
#
# name=input('entre name ')
# age=input('entre age ')
# number=input('entre number ')
#
#
#
#
#     # TODO 5 define a method to enroll new course to student courses list
# def enroll_new_object(self):
#         return self. C_list.append()
#
#
#     # method to get_student_details as dict
#     def get_student_details(self):
#         return self.__dict__
#
#
#     # method to get_student_courses
#     def get_student_courses(self):
#
#         # TODO 6 print student courses with their marks
#
#         def print_courses(self):
#             for course in self.courses:
#                 print(f"{course.number}: {course.mark}")
#
#     # method to get student_average as a value
#     def get_student_average(self):
#         total_marks = 0
#         for course in self.courses:
#             total_marks += course.mark
#         return total_marks / len(self.courses)
#
#
#         # TODO 7 return the student average
#         return total_marks / len(self.courses)
#
#
# # in Global Scope
# # TODO 8 declare empty students list
# Students=[]
#
# while True:
#
#     # TODO 9 handle Exception for selection input
#     selection = int(input("1.Add New Student\n"
#                           "2.Delete Student\n"
#                           "3.Display Student\n"
#                           "4.Get Student Average\n"
#                           "5.Add Course to student with mark.\n"
#                           "6.Exit"))
#
#     if selection == 1:
#         # code for adding new student
#         pass
#     elif selection == 2:
#         # code for deleting a student
#         pass
#     elif selection == 3:
#         # code for displaying a student
#         pass
#     elif selection == 4:
#         # code for getting student average
#         pass
#     elif selection == 5:
#         # code for adding course to student with mark
#         pass
#     elif selection == 6:
#         # exit the program
#         print("Exiting program...")
#     else:
#         # handle invalid input
#         print("Invalid selection. Please enter a number between 1 and 6.")
#
#
#
#         # TODO 10 make sure that Student number is not exists before
#         student_number = input("Enter Student Number")
#
#         student_name = input("Enter Student Name")
#         while True:
#             try:
#                 student_age = int(input("Enter Student Age"))
#                 break
#             except:
#                 print("Invalid Value")
#                 if not any(students.student_number == "1234" for students in students):
#
#
#         # TODO 11 create student object and append it to students list
#         new_student = Student("1234", "John Doe", 20)
#      students.append(new_student)
#
#      print("Student Added Successfully")
#
#     elif selection == 2:
#         student_number = input("Enter Student Number")
#         # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
# found = False
# for student in students:
#     if student.student_number == "1234":
#         students.remove(student)
#         found = True
#         break
#
# if found:
#     print("Student successfully deleted")
# else:
#     print("Student not Exist")
#
#     elif selection == 3:
#       student_number = input("Enter Student Number")
#         # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
# found = False
# for student in students:
#     if student.student_number == "1234":
#         print("Student Name:", student.name)
#         print("Student Number:", student.student_number)
#         print("Student GPA:", student.gpa)
#         found = True
#         break
#
# if not found:
#     print("Student Not Exist")
#     elif selection == 4:
#         student_number = input("Enter Student Number")
#         # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
#
# found = False
# for student in students:
#     if student.student_number == "1234":
#         total_gpa = sum(student.gpa_list)
#         average_gpa = total_gpa / len(student.gpa_list)
#         print("Student Name:", student.name)
#         print("Student Number:", student.student_number)
#         print("Student Average GPA:", average_gpa)
#         found = True
#         break
#
# if not found:
#     print("Student Not Exist")
#
#
#     elif selection == 5:
#         student_number = input("Enter Student Number")
#         # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
#
# new_course = Course(course_name, course_mark)
# student.courses.append(new_course)
#
# total_gpa = sum(student.gpa_list)
# average_gpa = total_gpa / len(student.gpa_list)
# print("Student Name:", student.name)
# print("Student Number:", student.student_number)
# print("Student Average GPA:", average_gpa)
# found = True
#  break
#
# if not found:
#     print("Student Not Exist")
#     else:
#         # TODO 16 call a function to exit the program
# import sys
# def exit_program () :
#     return sys.exit()