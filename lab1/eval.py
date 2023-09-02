# def factorials(num):
#     while(num!=1):
#         fact = num*(factorials(num-1))
#     return fact

def generate_factorial_between(n, m):
    factorial = []
    for num in range(n, m + 1):
        fact = num*(num-1)
        factorial.append(fact)
    return factorial

n = int(input("Enter the lower limit (n): "))
m = int(input("Enter the upper limit (m): "))

factorials = generate_factorial_between(n, m)
print("Factorial of numbers between", n, "and", m, "are:", factorials)