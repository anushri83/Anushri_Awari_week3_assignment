#Implement a program that calculates the Fibonacci sequence up to a specified number
#using both iterative and recursive approaches.

#_______  ITERATIVE FUNCTION   _________

def fibonacci_iterative(n1):
    if n1<=0:
        print("Input should be a positive integer.")

    elif n1==1:
        print(0)

    else:  
        a=0
        b=1
        for i in  range(2,n1):
            c=a+b
            a=b
            b=c
            print(c)

range1=int(input("Enter number: "))
fibonacci_iterative(range1)
    




#_______  RECUSRIVE FUNCTION   _________

def fibonacci_recursive(n):
   if n <= 1:
       return n
   
   else:
       return(fibonacci_recursive(n-1) + fibonacci_recursive(n-2))

range2 = int(input("Enter number: "))

if range2 <= 0:
   print("Plese enter a positive integer")

else:
   print("Fibonacci sequence:")
   for i in range(range2):
       print(fibonacci_recursive(i))