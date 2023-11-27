def p_occurance(a, b, c):
    p_occurance = (a > 0) + (b > 0) + (c > 0)
    return p_occurance == 2


print(p_occurance(2, 4, -3))    #return of the output
print(p_occurance(-4, 6, 8))    #return of the output
print(p_occurance(4, -6, 9))    #return of the output
print(p_occurance(-4, 6, 0))    #return of the output
print(p_occurance(4, 6, 10))     #return of the output
print(p_occurance(-14, -3, -4))   #return of the output
print(p_occurance(-100, -215, -888))   #return of the output
print(p_occurance(2, 16, 12))   #return of the output