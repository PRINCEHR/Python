class Animal(object):
    def __init__(self, species):
        self.species = species
    def display(self):
        print(self.species)

obj = Animal(species="Lion")
obj.display()

class Parent(object):
    def __init__(self):
        print("Parent")
    def parentfunc(self):
        print("Parent Fun")

class Child(Parent):
    def __init__(self):
        print("You Are In child")

objp = Parent()
objc = Child()

objc.parentfunc()

print(type(objc))
print(type(objp))

print(type(Parent))

class Parent(object):
    color = input("Enter color")
    def __init__(self, height,color):
        self.height = height
        self.color = color
    def display(self):
        print("Color:" +self.color)
        print("Height:" + self.height)

objp =Parent(5.6)
objp.display()
