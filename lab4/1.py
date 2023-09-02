import math

# Accept a number from the user
num = float(input("Enter a number: "))

# Calculate and print the sin value
sin_value = math.sin(num)
print(f"Sine value of {num} is {sin_value}")

# Check if the number is positive before calculating log and square root
if num > 0:
    # Calculate and print the natural logarithm (base e) value
    log_value = math.log(num)
    print(f"Natural logarithm of {num} is {log_value}")

    # Calculate and print the square root value
    sqrt_value = math.sqrt(num)
    print(f"Square root of {num} is {sqrt_value}")
else:
    print("Logarithm and square root are not defined for non-positive numbers.")
