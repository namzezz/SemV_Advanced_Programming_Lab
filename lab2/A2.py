def find_union(list1, list2):
    union = list1.copy()
    for item in list2:
        if item not in union:
            union.append(item)
    return union

def find_intersection(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

def find_difference(list1, list2):
    difference = []
    for item in list1:
        if item not in list2 and item not in difference:
            difference.append(item)
    return difference

# Taking input lists as strings and converting them to lists of integers
input_str1 = input("Enter the first list of integers separated by spaces: ")
input_str2 = input("Enter the second list of integers separated by spaces: ")
list1 = [int(x) for x in input_str1.split()]
list2 = [int(x) for x in input_str2.split()]

# Calculating and printing the union, intersection, and difference
union_result = find_union(list1, list2)
intersection_result = find_intersection(list1, list2)
difference_result = find_difference(list1, list2)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)
