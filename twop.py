def p_occurance(a, b, c):
    p_occurance = (a > 0) + (b > 0) + (c > 0)
    return p_occurance == 2


print(p_occurance(2, 4, -3))    
print(p_occurance(-4, 6, 8))    
print(p_occurance(4, -6, 9))    
print(p_occurance(-4, 6, 0))   
print(p_occurance(4, 6, 10))    
print(p_occurance(-14, -3, -4)) 
print(p_occurance(-100, -215, -888)) 
print(p_occurance(2, 16, 12)) 