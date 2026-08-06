try:
    num = int(input("Type a number "))
    result = 0
    digit = len(str(num))

    t = num
    while t > 0:
        digits = num % 10
        result = digits ** digit
        t // 10
        
    if num == result:
        print("Its a armstrong number ", num) 
    else:
        print("its not")  
except ValueError:
    print("wrong input try again") 