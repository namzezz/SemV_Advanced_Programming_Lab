# n=True
# m=False
# print(n+m)
# print("Hello World!")
# print(len("Hello World!"))
# name='Reiko'
# print(f'she said her name is {name}')
# input_string_var = input("Enter some data: ") 
# some_var=5

L1=[1,2,3,4,5]
L2=[6,7,8,9,10]
le=[n for n in L1 if n%2]+[n for n in L2 if not n%2]
print(le)
