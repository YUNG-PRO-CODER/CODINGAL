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