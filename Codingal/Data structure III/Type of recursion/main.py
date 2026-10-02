# tail recusion 

def b(n):
    if n == 1:
        return 1
    else:
        return n * b(n - 1)
        
print(b(4))

# non - tail recursion

def m(n):
    if n == 1:
        return 1
    print(n)
    return n * m(n - 1)

print(m(4))


#tree recursion

def q(n):
    if n == 1:
        return 1
    else:
        return q(2) + q(2)
print()
    

