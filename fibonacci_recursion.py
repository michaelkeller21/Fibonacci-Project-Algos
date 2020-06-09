def fibonacci_recursion(n):
    if n<=1:
        return n
    else:
        return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
