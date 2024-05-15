# write a function that takes an interger as an argument and returns if it's in the power of 2
import math

def is_power_of_two(number):
    sqrt = int(math.sqrt(number))
    if sqrt * sqrt == number:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_power_of_two(8))