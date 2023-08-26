def fibonacci_cached(n, cache={}):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_cached(n - 1) + fibonacci_cached(n - 2)
    
    cache[n] = result
    return result

n = int(input("Enter the value of n: "))
print(f"The {n}-th Fibonacci number is:", fibonacci_cached(n))
