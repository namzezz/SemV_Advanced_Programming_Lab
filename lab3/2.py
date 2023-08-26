def unique_elements(input_list):
    unique_list=[]
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


input_str= input("Enter the list of elements: ")
input_list= input_str.split()

input_list=[int(element) for element in input_list]

result = unique_elements(input_list)
print("list with unique elements: ", result)