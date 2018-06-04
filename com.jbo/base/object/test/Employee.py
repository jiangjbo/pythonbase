#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ",Salary: ", self.salary


# 创建 Employee 类的第一个对象
emp1 = Employee("Zara", 200)
emp2 = Employee("Manni", 500)
emp1.displayEmployee()
emp2.displayCount()
print "Total Employee %d" % Employee.empCount

emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__



