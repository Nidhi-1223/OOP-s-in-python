from cgi import print_arguments
from traceback import StackSummary


class Student:
    school_name = 'ABC School'          #class variables

    def __init__(self,name, age):       #constructor to initialize instance variables
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, name):       #cls refers to the class
        print(Student.school_name)      #access class variables
        Student.school_name = name      #modify class variable

jessa = Student('Jessa',14)
Student.change_school('XYZ School')
print(jessa.school_name)