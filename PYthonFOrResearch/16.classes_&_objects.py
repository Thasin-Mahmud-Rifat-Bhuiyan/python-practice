# Class and Object


class Student:
    # class variable (shared for all objects)
    school = "ABC School"

    # constructor
    def __init__(self, name, age):
        # instance variables (different for each object)
        self.name = name
        self.age = age

    # method
    def show(self):
        print(self.name, self.age, self.school)


# creating objects
s1 = Student("Rahim", 20)
s2 = Student("Karim", 22)

s1.show()
s2.show()
