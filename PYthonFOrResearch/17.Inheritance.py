# parent class
class Animal:
    def speak(self):
        print("Animal sound")


# child class
class Dog(Animal):
    def bark(self):
        print("Barking")


d = Dog()
d.speak()
d.bark()
