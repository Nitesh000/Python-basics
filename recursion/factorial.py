import sys
sys.setrecursionlimit(10000) #just setting a limiting value from preventing the inifinite loop

def factorial(n):
    print(n)
    if int(n) == n:
        if n in [0,1]:
            return 1
        elif n < 0:
            print(f"Please enter a positive integer {n}")
        else:
            return n * factorial(n - 1)
    else: 
        print(f"Please enter an integer value not {n}")

fact = factorial(3)
print(f"The fact is {fact}")
fact1 = factorial(0)
print(f"The fact is {fact1}")
fact2 = factorial(-1)
fact3 = factorial(1.2)
