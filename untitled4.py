# -*- coding: utf-8 -*-
"""
Created on Thu May 27 16:30:19 2021

@author: SST-LAB
"""

class employee:
    empCount=-0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        employee.empCount=+1
    def displayCount(self):
        print(f"Total employee {employee.empCount}")
    def diisplayEmployee(self):
        print(f"Name:{self.name} salary:{self.salary}")
emp1= employee(str(input("enter name:"  )),int(input("enter salary:"  )))
emp2=employee(str(input("enter name:"  )),int(input("enter salary:"  )))
emp1.diisplayEmployee()
emp2.diisplayEmployee()
print(f"Total employee{employee.empCount}")
