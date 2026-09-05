def main(n, q) -> int:
    o = n ^ q
    
    print(o)
    
    if o == 1:
        return("the value is 1")
    elif o == 0:
        return("the value is 0")


while True:
    try:
        n = int(input("Type a number: "))
        q = int(input("Type another number: "))
        print(main(n,q))
        
    except ValueError:
        print("try again")