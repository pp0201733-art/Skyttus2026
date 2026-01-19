# 1. Car Class (accelerate / brake)

class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 5

c = Car("Tata", "Nexon")
c.accelerate()
c.brake()
print(c.speed)

# 2. BankAccount Class (deposit / withdraw)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(300)
print(acc.balance)

# 3. Student Class (average marks)

class Student:
    def average(self, m1, m2, m3):
        return (m1 + m2 + m3) / 3

s = Student()
print(s.average(70, 80, 90))

# 4.  Rectangle Class (area & perimeter)

class Rectangle:
    def area(self, l, b):
        return l * b

    def perimeter(self, l, b):
        return 2 * (l + b)

r = Rectangle()
print(r.area(5, 4))
print(r.perimeter(5, 4))

# 5. Employee Class (salary details)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

e = Employee("Payal", 30000)
e.display()

# 6. Book Class (details)

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        print(self.title, self.author, self.price)

b = Book("Python", "Hetal", 500)
b.show()

# 7. Circle Class (area & circumference)

class Circle:
    def area(self, r):
        return 3.14 * r * r

    def circumference(self, r):
        return 2 * 3.14 * r

c = Circle()
print(c.area(7))
print(c.circumference(7))

# 8. Laptop Class (apply discount)

class Laptop:
    def __init__(self, price):
        self.price = price

    def discount(self, d):
        return self.price - (self.price * d / 100)

l = Laptop(50000)
print(l.discount(10))

# 9. Flight Class (seat booking)

class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat Booked")
        else:
            print("No seats")

f = Flight(2)
f.book()
f.book()
f.book()

# 10.Shop Class (add & list products)

class Shop:
    def __init__(self):
        self.products = []

    def add(self, item):
        self.products.append(item)

    def show(self):
        print(self.products)

s = Shop()
s.add("Pen")
s.add("Book")
s.show()

    