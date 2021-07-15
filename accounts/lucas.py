import math
def is_prime_fast(n):
    if n <= 1:
        
        return False
    if n == 2:
        print("tru")
        return True
    if n > 2 and n % 2 == 0:
        
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            
            return False
    
    return True

def is_prime(num):
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                return False 
        else:
            return True
         
    else:  
        return False

if is_prime_fast(175)==is_prime(175):
    print("1")