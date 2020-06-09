def fibonacci_memoization(n):
    fib_cache=[]

    if n<=1:
        return n

    else: 
        fib_cache.append(1)
        fib_cache.append(1)
        for i in range (2, n):
            fib_cache.append(fib_cache[i-1]+fib_cache[i-2])
        return fib_cache[n-1]
    