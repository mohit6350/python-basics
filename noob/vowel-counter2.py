# This is an improved version of the vowel counter

def vowel_counter(input):
    input = str.lower(input)
    
    a,e,i,o,u = 0,0,0,0,0
    
    for alpha in input:
        if alpha == 'a':
            a += 1
        elif alpha == 'e':
            e += 1
        elif alpha == 'i':
            i += 1
        elif alpha == 'o':
            o += 1
        elif alpha == 'u':
            u += 1    
            
    print(f"Total vowels found : {a+e+i+o+u}")
    print(f"Total A : {a}")
    print(f"Total E : {e}")
    print(f"Total I : {i}")
    print(f"Total O : {o}")
    print(f"Total U : {u}")
    
if __name__ == "__main__":
    vowel_counter("mohit KHARE")
        