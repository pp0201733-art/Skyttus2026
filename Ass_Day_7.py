# 1. Animal → Dog, Cat (Inheritance)
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.sound()
c.sound()

# 2. Vehicle → Car → ElectricCar (Hierarchy)

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def fuel(self):
        print("Car uses fuel")

class ElectricCar(Car):
    def charge(self):
        print("Electric car uses battery")

e = ElectricCar()
e.move()
e.fuel()
e.charge()

# 3. Method Overriding

class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def show(self):
        print("Child class")

c = Child()
c.show()

# 4. Multiple Inheritance

class Father:
    def skill(self):
        print("Driving")

class Mother:
    def hobby(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
c.hobby()

# 5. Polymorphism (Shapes)

class Shape:
    def area(self):
        print("Area")

class Square(Shape):
    def area(self):
        print("Square area")

class Circle(Shape):
    def area(self):
        print("Circle area")

for s in (Square(), Circle()):
    s.area()

# 6.  Bank System

class Bank:
    def account(self):
        print("Bank Account")

class SavingsAccount(Bank):
    def account(self):
        print("Savings Account")

class CurrentAccount(Bank):
    def account(self):
        print("Current Account")

SavingsAccount().account()
CurrentAccount().account()

# 7. Private Variable (Getter / Setter) 

class Person:
    def __init__(self):
        self.__age = 20

    def get_age(self):
        print(self.__age)

    def set_age(self, a):
        self.__age = a

p = Person()
p.get_age()
p.set_age(25)
p.get_age()

# 8.Teacher → Student  

class Teacher:
    def teach(self):
        print("Teaching")

class Student(Teacher):
    def study(self):
        print("Studying")

s = Student()
s.teach()
s.study()

# 9. MusicPlayer → Spotify (Override)

class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing on Spotify")

s = Spotify()
s.play()

# 10. super() Example

class A:
    def __init__(self):
        print("Class A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B")

b = B()
    