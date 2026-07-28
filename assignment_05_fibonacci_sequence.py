# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_fibonacci_sequence(n):
    if n == 1:
        return [0]
    
    sequence = [0, 1]
    a, b = 0, 1
    
    for _ in range(2, n):
        next_term = a + b
        sequence.append(next_term)
        a, b = b, next_term
        
    return sequence

def is_fibonacci_number(num):
    if num < 0:
        return False
    if num == 0 or num == 1:
        return True
        
    a, b = 0, 1
    while b < num:
        next_term = a + b
        a = b
        b = next_term
        
    return b == num

if _name_ == "_main_":
    print("--- PART A: Print the First N Terms ---")
    terms_input = int(input("How many terms? "))
    
    if terms_input <= 0:
        print("Error: The number of terms must be a positive integer.")
    else:
        fib_list = get_fibonacci_sequence(terms_input)
        print("Fibonacci sequence:", " ".join(map(str, fib_list)))
        
    print("\n--- PART B: Check if a Number Belongs to the Sequence ---")
    check_input = int(input("Enter a number to check: "))
    
    if is_fibonacci_number(check_input):
        print(f"{check_input} is a Fibonacci number.")
    else:
        print(f"{check_input} is NOT a Fibonacci number.")
