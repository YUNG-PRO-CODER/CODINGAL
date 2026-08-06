"""armstrong number"""

try:
    
    num = int(input("Type a number "))
    result = 0
    digit = len(str(num))

    t = num
    while t > 0:
        digits = t % 10
        result += digits ** digit
        t = t // 10
        
    if num == result:
        print("Its a armstrong number ", num) 
    else:
        print("its not", num)  
        
except ValueError:
    print("wrong input try again") 
    
"""factors"""


try:     
    def print_factors(num):
            
            for i in range(1, num + 1):
                if num % i == 0:
                    result = num // i
                    print(result)
    print_factors(20)        
            
except ValueError:
    print("try again")

