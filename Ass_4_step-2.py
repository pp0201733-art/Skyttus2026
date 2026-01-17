# 1 eligible vote number
age = int(input("Enter age:"))
if age >= 18:
    print("Eligible to vote ")
else:
    print("Not Eligible to vote")

# 2 calculator marks
marks = int(input("Enter marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")

# 3 simulate traffic color
color =input("Enter traffic light colr:")
if color == "red":
    print("stop")
elif color == "yellow":
    print("wait")
elif color == "green":
    print("go")
else:
    print("invalid color ")
# 4 ATM withadraw 
blance = 10000
withdraw = int(input("Enter withdraw amount :"))
if withdraw <= blance:
    print("withdraw successful")
else:
    print("insufficient blance")


# 5 cheack numbers positive and nagative
num =int(input("Enter number :"))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Nagetive  number")
else:
    print("zero")

# 6 check within range
num =int(input("Enter Number :"))
if num >= 10 and num <= 50:
    print("Number is within range")
else:
    print("Number is outside range ")


# 7 verification
username = input("Enter userName :")
password = input(" Enter Passwoed :")

if username == "admin" and password == "1234":
    print("login successfull")
else:
    print("invalide login")

# 8  electricity bill calculator
units = int(input("Enter units : "))
if units >= 100:
    bill = units * 1
elif units <=200:
    bill = units * 2
else :
    bill = units * 3
print("Electricity bill =",bill)


# 9 simple calculation oprators
a = int(input("Enter first Number :"))
b = int(input("Enter Second Number :"))

op = input("Enter Oparation(+,-,*,/):")
if op == "+":
    print(a+b)
elif op =="-":
    print(a-b)
elif op =="*":
    print(a*b)
elif op =="/":
    print(a/b)   
else :
    print("invalide opartion")

# 10   check triangle
a = int(input("Enter side 1 :"))
b = int(input("Enter side 2 :"))
c = int(input("Enter side 3 :"))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("isoscales Triangle")
else:
    print("scalene Triangle")    