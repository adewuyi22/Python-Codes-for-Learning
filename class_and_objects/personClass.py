class Person:

    #declaring a function
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj=Person("John", "Doe")
print(obj.name)
print(obj.age)


class Student:
    #declaring a function
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj=Student("\nBetty", "James")
print(obj.name)
print(obj.age)
