def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    """
    As described by Fibo et al.
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        result.append(123)        
    return result
