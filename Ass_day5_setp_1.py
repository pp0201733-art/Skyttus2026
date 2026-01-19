#1 Division by Zero Error Handle
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
    
#2 Invalid Integer Input Handle

 try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid integer input")
    
# 3 File Not Found Error Handle
try:
    f = open("demo.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Error: File not found")
    
# 4  Multiple Exception Blocks    
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# 5.  finally Block for Cleanup    
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Zero division error")
finally:
    print("Program finished")
    
# 6.  Custom Exception (Invalid Age < 18) 

class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError
    print("Valid age")
except AgeError:
    print("Invalid age! Age must be 18 or above")
    
# 7. IndexError Handle

try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")
    
# 8. Two Numbers – All Possible Errors   

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except (ValueError, ZeroDivisionError):
    print("Error occurred")
    
# 9.  Log Errors to File

  try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)
except Exception as e:
    f = open("error.log", "w")
    f.write(str(e))
    f.close()
    print("Error logged to file")  

# 10.Email Validation with Exception

try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email:
        raise ValueError
    print("Valid email")
except ValueError:
    print("Invalid email format")     