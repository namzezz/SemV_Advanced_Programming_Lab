# a) Create a text file with minimum eight lines
with open("sample.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Python is amazing\n")
    file.write("OpenAI's GPT-3.5 is powerful\n")
    file.write("Coding is fun\n")
    file.write("Programming is a valuable skill\n")
    file.write("Learning never stops\n")
    file.write("Data science is in demand\n")
    file.write("Practice makes perfect\n")

# b) Read the data from the file
with open("sample.txt", "r") as file:
    lines = file.readlines()

# c) Store the data in dictionary form with line numbers as keys
lengths_dict = {}
for idx, line in enumerate(lines, start=1):
    lengths_dict[str(idx)] = [len(line.strip())]

print("Dictionary with line numbers as keys and lengths as values:")
print(lengths_dict)

# d) Create a dictionary with letters as keys and frequencies as values
letters_dict = {}
for line in lines:
    for char in line:
        if char.isalpha():
            char = char.lower()
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1

print("\nDictionary with letters as keys and frequencies as values:")
print(letters_dict)
