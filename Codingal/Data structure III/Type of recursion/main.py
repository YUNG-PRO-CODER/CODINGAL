# tail recusion 

def b(n, result=1):
    if n == 1:
        return result
    return b(n - 1, result * n)

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
    return q(n - 1) + q(n - 1)

print(q(4))




