# Write a Python function called sum_of_squares that takes a positive integer n as an argument and returns the sum of the squares of all the integers from 1 to n (inclusive).

# For example, if n is 3, the function should return 1^2 + 2^2 + 3^2 = 14.

# Your task is to implement the sum_of_squares function using a for loop.

# first iterate over the numbers
# square the number and store in a temp variable
# add the temp to the new value of the square 

temp = 0
def sum_of_squares(number):
    global temp
    
    for n in range(number):
        temp = temp + (n * n)   

    print(temp)
    temp = 0

if __name__ == "__main__":
    sum_of_squares(4)
