def is_hexadecimal(s):
    try:
        int(s, 16)  # Try to convert the string to an integer in base 16
        return True
    except ValueError:
        return False

input_str = input("Enter a string: ")

if is_hexadecimal(input_str):
    print(f"'{input_str}' is a hexadecimal number.")
else:
    print(f"'{input_str}' is not a hexadecimal number.")
