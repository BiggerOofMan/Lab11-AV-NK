# https://github.com/BiggerOofMan/Lab11-AV-NK
# Partner 1: Anirudh S. Vijayaraman
# Partner 2: Dropping the Lab

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): 
    pass

def sub(a, b): 
    pass
    
def mul(a, b): 
    pass
    
def div(a, b): 
    pass
    
def log(a, b): 
    pass
    
def exp(a, b): 
    pass

def square_root(a):
    if a < 0:
        raise ValueError("math domain error: square root of negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("invalid base or argument for logarithm")
    return math.log(b, a)


def exponent(a, b):
    return a ** b



