
#Create a Python module that contains functions for common mathematical operations (e.g.,
#factorial, greatest common divisor). Write a script that imports this module and uses its functions.


#Creation of modules:-

def factorial(num):
    if num < 0:
        return "Negative numbers are invalid."
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def power(base, exponent):
    return base ** exponent


def lcm(a, b):
    return abs(a * b) // greatest_common_divisor(a, b)


#This modules will be imported and used in main.py file