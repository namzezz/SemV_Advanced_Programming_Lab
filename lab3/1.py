def multiply_list(numbers):
    result=1
    for num in numbers:
        result*=num
    return result

input_str= input("Enter a list of numvbers: ")
input_numbers = [int(x) for x in input_str.split()]

output = multiply_list(input_numbers)
print("The product of the numbers is:", output)