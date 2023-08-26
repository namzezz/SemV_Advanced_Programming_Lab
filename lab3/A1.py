def count_upper_lower(text):
    uc = 0
    lc = 0
    
    for char in text:
        if char.isupper():
            uc += 1
        elif char.islower():
            lc += 1
    return uc, lc

input_text = input("Enter the string: ")
upper, lower = count_upper_lower(input_text)

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
