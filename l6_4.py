pip install pymysql
import _mysql

class Parent(object):
    stream ="Btech"
    def __init__(self):
        print("Parenet Constructor")
    def display(self):
        print("Parent Display Function")

class Child(Parent):
    def __init__(self):
        print("Child Constructor")
    def display(self):
        super().display()
        print("Child Display")

objc = Child()
objc.display()