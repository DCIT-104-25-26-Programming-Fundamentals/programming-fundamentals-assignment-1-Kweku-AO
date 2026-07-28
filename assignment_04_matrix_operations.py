# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))
    print()

def input_matrix(rows, cols, name="Matrix"):
    """Helper function to read a matrix from the user row by row."""
    print(f"\nEntering values for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").split()
            if len(row_input) == cols:
                matrix.append([int(x) for x in row_input])
                break
            print(f"Error: You must enter exactly {cols} values.")
    return matrix

def transpose_matrix(matrix):
    """Computes the transpose of an M x N matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    
    result = [[0] * rows for _ in range(cols)]
    
    for r in range(rows):
        for c in range(cols):
            result[c][r] = matrix[r][c]
            
    return result

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = [[0] * cols for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            result[r][c] = matrix_a[r][c] + matrix_b[r][c]
            
    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = [[0] * cols_b for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
                
    return result

if _name_ == "_main_":
    print("--- PART A: Transpose a Matrix ---")
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    mat_a = input_matrix(r, c, "Matrix A")
    
    print("\nOriginal Matrix:")
    print_matrix(mat_a)
    
    transposed = transpose_matrix(mat_a)
    print("Transposed Matrix:")
    print_matrix(transposed)
    
    print("--- PART B: Add Two Matrices ---")
    print(f"Let's enter a second matrix of the same size ({r}x{c}) to add.")
    mat_b = input_matrix(r, c, "Matrix B")
    
    sum_result = add_matrices(mat_a, mat_b)
    print("\nSum of Matrix A and Matrix B:")
    print_matrix(sum_result)
    
    print("--- PART C: Multiply Two Matrices ---")
    print(f"Matrix A is currently {r}x{c}. To multiply, Matrix C must have {c} rows.")
    c_cols = int(input(f"Enter number of columns for Matrix C: "))
    mat_c = input_matrix(c, c_cols, "Matrix C")
    
    product_result = multiply_matrices(mat_a, mat_c)
    print(f"\nProduct of Matrix A ({r}x{c}) × Matrix C ({c}x{c_cols}):")
    print_matrix(product_result)
