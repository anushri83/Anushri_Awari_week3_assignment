# Write a program that defines a function to check whether a number is prime. Use this function in a
# script to find all prime numbers within a given range.

def check_prime(n):

    if n <= 1:
        return False
    
    for i in range(2, int(n//2) + 1):  
        if n % i == 0:
            return False
        
    return True

def find_primes_in_range(start, end):
    
    primes = []
    for i in range(start, end):
        if check_prime(i):
            primes.append(i)
    return primes


start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

primes_in_range = find_primes_in_range(start_range, end_range)

if primes_in_range:
    print(f"Prime numbers between {start_range} and {end_range} are: {primes_in_range}")
    
else:
    print(f"There are no prime numbers between {start_range} and {end_range}.")
