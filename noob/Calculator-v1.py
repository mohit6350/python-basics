# This is the version 1, simple and nothing fancy

# Prompting user for inputs
number1 = input("Enter first number : ")
number2 = input("Enter second number : ")

# Providing user choice
print("your options -> ")
print("1. Add")
print("2. Sub")
print("3. Div")
print("4. Mul")

choice = int(input("Please enter a number from 1 to 4 : "))

# Defining the Add function
def addition(number1, number2):
    return int(number1) + int(number2)

# Defining the Sub function
def subtraction(number1, number2):
    return int(number1) - int(number2)

# Defining the Mul function
def multiplication(number1, number2):
    return int(number1) * int(number2)

# Defining the Div function
def division(number1, number2):
    return int(number1) / int(number2)

# Conditionals check
if choice == 1:
    print(addition(number1, number2))
elif choice == 2:
    print(subtraction(number1, number2))    
elif choice == 3:
    print(multiplication(number1, number2))
elif choice == 4:
    print(division(number1, number2))
else:
    print("Invalid input : number range (1-4)")    



