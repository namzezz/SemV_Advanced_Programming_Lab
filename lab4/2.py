import cmath

# Accept a complex number from the user
input_str = input("Enter a complex number (in the format a+bj): ")
try:
    complex_num = complex(input_str)
except ValueError:
    print("Invalid input. Please enter a complex number in the format a+bj.")
else:
    # Calculate and print the sine value of the complex number
    sin_value = cmath.sin(complex_num)
    print(f"Sine value of {complex_num} is {sin_value}")

    # Calculate and print the natural logarithm value of the complex number
    log_value = cmath.log(complex_num)
    print(f"Natural logarithm of {complex_num} is {log_value}")

    # Calculate and print the square root value of the complex number
    sqrt_value = cmath.sqrt(complex_num)
    print(f"Square root of {complex_num} is {sqrt_value}")
