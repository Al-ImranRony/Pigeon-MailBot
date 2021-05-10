#Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I'm {self.name} and {self.age} years old.")


class Cat(Pet):
    def sound(self):
        print("Meow")

class Dog(Pet):
    def sound(self):
        print("Bark")

#Class method and attributes
class Person:
    numbers = 2
    gravity = 9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        return cls.numbers

    @classmethod
    def add_person(cls):
        cls.numbers += 1

    @staticmethod
    def add_more(n):
        return n + 5


p = Pet("Ghuri", 5)
p.info()
c = Cat("Catter", 4)
c.sound() 

p1 = Person("Ron")
print(Person.number_of_people())

print(Person.add_more(2))