# Encapsulation example


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private variable (encapsulation)

    # method to get age
    def get_age(self):
        return self.__age

    # method to set age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")


# creating object
s1 = Student("Rahim", 20)

print(s1.name)

# accessing private data using method
print(s1.get_age())

# changing age using method
s1.set_age(25)
print(s1.get_age())
