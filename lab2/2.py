def read_matrix():
    rows, cols = map(int, input("Enter the number of rows and columns: ").split())
    matrix = {}
    
    for i in range(rows):
        row = list(map(int, input(f"Enter values for row {i + 1}: ").split()))
        for j, value in enumerate(row):
            if value != 0:
                matrix[(i, j)] = value
                
    return matrix, rows, cols

def add_matrices(matrix1, matrix2, rows, cols):
    result_matrix = {}
    
    for i in range(rows):
        for j in range(cols):
            value1 = matrix1.get((i, j), 0)
            value2 = matrix2.get((i, j), 0)
            result = value1 + value2
            if result != 0:
                result_matrix[(i, j)] = result
                
    return result_matrix

def display_matrix(matrix, rows, cols):
    for i in range(rows):
        row = []
        for j in range(cols):
            value = matrix.get((i, j), 0)
            row.append(value)
        print(" ".join(map(str, row)))

# Read the first matrix
print("Enter details for Matrix 1:")
matrix1, rows, cols = read_matrix()

# Read the second matrix
print("Enter details for Matrix 2:")
matrix2, _, _ = read_matrix()

# Add the matrices
result_matrix = add_matrices(matrix1, matrix2, rows, cols)

# Display the result matrix
print("Resultant matrix:")
display_matrix(result_matrix, rows, cols)
