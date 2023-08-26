def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j] for j in range(i + 1)]
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

n = int(input("Enter the number of rows for Pascal's triangle: "))
pascal_triangle = generate_pascal_triangle(n)
print_pascal_triangle(pascal_triangle)
