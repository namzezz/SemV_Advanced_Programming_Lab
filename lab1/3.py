n=int(input("Enter the number of strings: "))
strings=[]

for i in range(n):
    strings.append(input("Enter a string: "))
    
    
count_same_first_last=0
for string in strings:
    if len(string)>=2 and string[0]==string[-1]:
        count_same_first_last+=1
        
print("Number of strings with the same first and last character: ", count_same_first_last)


print("Strings with odd length: ")
for string in strings:
    if len(string)%2!=0:
        print(string)