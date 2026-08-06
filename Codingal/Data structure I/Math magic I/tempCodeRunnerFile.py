try:
        
    
    def print_factors(num):
            
            for i in range(1, num + 1):
                if num % i == 0:
                    result = num // i
                    print(result)
    print_factors(20)        
            
except ValueError:
    print("try again")