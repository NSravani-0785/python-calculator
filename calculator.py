import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Cannot find square root of negative number."
    return math.sqrt(a)

def percentage(value, percent):
    return value * percent / 100

def modulus(a, b):
    if b == 0:
        return "Cannot perform modulus by zero."
    return a % b

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(int(n))
