def fibonacci(n):
    if n >= 0 and int(n) == n:
        if n in [0,1]:
            return n
        else: 
            return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        print("Pleae enter a non negative integer")
        
print(fibonacci(7))
print(fibonacci(-1))
fibonacci(1.3)
