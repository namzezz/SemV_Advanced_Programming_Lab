import A1m

# Input string
input_string = input("Enter a string: ")

# Reverse the string using the custom module
reversed_str = A1m.reverse_string(input_string)
print("Reversed string:", reversed_str)

# Check if the string is a palindrome using the custom module
if A1m.is_palindrome(input_string):
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")
