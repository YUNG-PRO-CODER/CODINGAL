#binary

def max_ones(mun):
    s = 0
    h = 0
    
    for nums in mun:
        if nums == 1:
            s += 1
        else:
            s = 0
        
        h = max(h, s)
        
    return h
        
print(max_ones([1,1,0,1,1,1,1]))

# moving zeros

def move_zeros(num):
    w = 0
    
    for scan in range(len(num)):
        if num[scan] != 0:
            num[w] = num[scan]
            w += 1
            
    num[w:] = [0] * (len(num) - w)
    
    return num    
    
        
print(move_zeros([1, 0, 0, 5, 0, 3, 2]))

# 
            
        