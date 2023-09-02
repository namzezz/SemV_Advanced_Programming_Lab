# string_utils.py

def reverse_string(input_string):
    """Reverse a given string."""
    return input_string[::-1]

def is_palindrome(input_string):
    """Check if a given string is a palindrome."""
    cleaned_string = ''.join(filter(str.isalnum, input_string)).lower()
    reversed_string = reverse_string(cleaned_string)
    return cleaned_string == reversed_string
