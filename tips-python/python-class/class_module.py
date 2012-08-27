#! /usr/bin/python
#=============================================================================
#     FileName:		class.py
#     Desc:		This is my first python for class 
#     Author:		forrest
#     Email:		hongsun924@gmail.com
#     HomePage:		NULL
#     Version:		0.0.1
#     LastChange:	2011-04-01 14:00:06
#     History:		
#=============================================================================

class School:
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def show_info(self):
        print "The Name is: %s;\n The ID is: %d" %(self.name, self.id)

class Teacher(School):
    def __init__(self, name, id, salary):
        School.__init__(self, name, id)
        self.salary=salary
    def show_info(self):
        print '''The Teachers Info as following:
        The Name is:    %s;
        The ID is:      %s;
        The Salary is:  %d;
        ''' %(self.name, self.id, self.salary)

class Student(School):
    def __init__(self, name, id, score):
        School.__init__(self, name, id)
        self.score=score
    def show_info(self):
        print '''The Students Info as following:
        The Name is:    %s;
        The ID is:      %s;
        The Score is:   %d;
        ''' %(self.name, self.id, self.score)

#info_teacher=Teacher("Robert", "123456", 8000)
#info_student=Student("Forrest", "998987", 90)

#info_teacher.show_info()
#info_student.show_info()
