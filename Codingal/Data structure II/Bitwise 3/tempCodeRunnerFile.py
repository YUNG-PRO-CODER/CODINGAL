 c = int(input("Type a value for division: "))
    d = int(input("Type the divisior of the divident: "))
    
    for i in range(31, -1, -1):
        b = (c >> i) & 1 
        print(b)