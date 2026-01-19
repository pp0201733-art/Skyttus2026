# 1.Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(is_prime(7))

# 2.Function to reverse a string

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# 3.  Function to find factorial

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(factorial(5))

#4. Function to calculate simple interest

def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(1000, 5, 2))

# 5.Function to check palindrome word

def is_palindrome(word):
    if word == word[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(is_palindrome("madam"))

# 6. Function to count vowels in a string

def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count

print(count_vowels("education"))

# 7.  Function to merge two lists

def merge_lists(a, b):
    return a + b

print(merge_lists([1, 2, 3], [4, 5]))

# 8. Function to find GCD of two numbers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18))

# 9.  Function to find area of rectangle

def rectangle_area(l, w):
    return l * w

print(rectangle_area(5, 4))

# 10. Function to check Armstrong number

def is_armstrong(n):
    temp = n
    s = 0
    while temp > 0:
        d = temp % 10
        s += d ** 3
        temp //= 10
    if s == n:
        return "Armstrong Number"
    else:
        return "Not Armstrong"

print(is_armstrong(153))