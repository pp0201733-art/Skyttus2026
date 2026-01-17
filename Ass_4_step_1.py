
#1 Print Number 1 To 10
for i in range(1, 11):
    print(i)

#2. Given Number 
n =int(input("Enter a number: "))

for i in range(1, 11):
    print(n , "x", i , "=" ,n * i)

#3 Fatorial Number
n =int(input(" Enter a number: "))
fact = 1 
for i in range( 1, n + 1 ):
    fact *= i
print("factorial =" , fact)

#4 Fibonacci Numbers
n =int(input("enter N: "))
a , b =0 , 1
print("fibonecci series :")
for i in range (n):
    print(a ,end =" ")
    a , b = b,a + b

#5 Check Prime Number
num =int(input("Enter a number:"))
flag = True
if num <=1:
    flag =False
else:
    for i in range(2 , num):
        if num % i ==0:
            flag =False
            break
if flag:
    print("prime number")
else:
    print("not a prime number ")


 #6 Reverse Number 
num =int(input("Enter a number:"))
rev = 0 
while num >0 :
    digit =num %10
    rev = rev  * 10 + digit
    num //= 10
print("reversed number :", rev)  

#7. Count digit
num =int(input(" enter a number :"))
count =0
while num >0:
    count += 1
    num //=10

print("total digit:", count)

#8. Finde Sum Even Number
sum_even =0
for i in range(1 ,100):
    if i % 2 == 0:
        sum_even += i
print("sum of even number:", sum_even)

#9. Pyramid Petten
rows =int(input(" enter rows :"))

for i in range(1, rows + 1):
    print("*" * i)

#10. Divisors Number 
num =int(input("enter a number:"))
print("divisors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
