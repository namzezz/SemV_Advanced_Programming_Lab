def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes_between(n, m):
    primes = []
    for num in range(n, m + 1):
        if is_prime(num):
            primes.append(num)
    return primes

n = int(input("Enter the lower limit (n): "))
m = int(input("Enter the upper limit (m): "))

prime_numbers = generate_primes_between(n, m)
print("Prime numbers between", n, "and", m, "are:", prime_numbers)
