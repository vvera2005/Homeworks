fib = {}

def fib_rec(n):
    if n in fib:
        return fib[n]
    if n == 1 or n == 2:
        x = 1
    if n > 2 :
        x = fib_rec(n-1) + fib_rec(n-2)
    
    fib[n] = x
    return x

print(fib_rec(5))
