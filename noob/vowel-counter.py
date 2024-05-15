# Write a function that takes string as an argument and return the total number of vowels in the string.

def vowel_counter(input):
    a,e,i,o,u = 0,0,0,0,0
    for alpha in input:
        if alpha == 'a' or alpha == 'A':
            a += 1
        elif alpha == 'e' or alpha == 'E':
            e += 1
        elif alpha == 'i' or alpha == 'I':
            i += 1
        elif alpha == 'o' or alpha == 'O':
            o += 1
        elif alpha == 'u' or alpha == 'U':
            u += 1
            
    print(f"Total vowels found : {a+e+i+o+u}")
    print(f"Total A : {a}")
    print(f"Total E : {e}")
    print(f"Total I : {i}")
    print(f"Total O : {o}")
    print(f"Total U : {u}")
    
    
if __name__ == "__main__":
    vowel_counter("MOHIT")