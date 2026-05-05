class Animal:
    def sound(self):
        print("Animal sound")


class Cat(Animal):
    def sound(self):
        print("Meow")  # overriding parent method


c = Cat()
c.sound()
