try:
    
    a = int(input("Type 'a' value: "))
    b = int(input("Type 'b' value: "))
    
    a =  a ^ b
    b =  a ^ b
    a = a ^ b
    
    print(a, b)
    
    
    c = int(input("Type a value for division: "))
    d = int(input("Type the divisor of the dividend: "))

    q = 0
    v = 0

    for i in range(c.bit_length() - 1, -1, -1):
        b = (c >> i) & 1
        v = (v << 1) | b

        if v >= d:
            v -= d
            q |= (1 << i)

    print("Quotient:", q)
        
        
    
except ValueError:
    print("try again")