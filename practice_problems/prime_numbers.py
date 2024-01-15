# Write a Python function named is_prime that takes a positive integer n as an argument and returns True if n is a prime number, and False otherwise. Then, write another function named print_primes that takes a positive integer m as an argument and prints all prime numbers from 1 to m.

# number = 3

def is_prime(n):
    if n == 1:
        return True
    
    for i in range(2,n):
        if (n % i == 0):
            return False 
    
    return True    
    

def print_primes(number):
    primes = []
    primes.append(1)
    primes.append(2)
    
    for i in range( 3 , number ):
        if is_prime(i) == True:
            primes.append(i) 
    
    return primes        
            
    
    
if __name__ == "__main__":
    print(f"{is_prime(9)}")
    print(f"{print_primes(10)}")