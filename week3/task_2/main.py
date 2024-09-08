#imported modules from task_2,py
from task_2 import factorial, greatest_common_divisor, power, lcm 

num = 5
print(f"The factorial of {num} is ",factorial(num))

a, b = 36, 60
print(f"The greatest common divisor of {a} and {b} is" ,greatest_common_divisor(a,b))

base, exponent = 2, 3
print(f"{base} raised to the power of {exponent} is" ,power(base,exponent))

a1, b1 = 12, 18
print(f"The least common multiple of {a} and {b} is" ,lcm(a1,b1))
