# Question: Multiplication Table

# Write a Python function called multiplication_table that takes a positive integer n as an argument and prints the multiplication table for numbers from 1 to n. The table should be formatted and displayed nicely.

def multiplication(n):
    for i in range(1,11):
        print(f"{i} * {n} = { i * n }")
        
        
if __name__ == "__main__":
    multiplication(5)
        