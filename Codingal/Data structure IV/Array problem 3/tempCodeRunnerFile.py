def max_ones(mun):
    s = 0
    h = 0
    
    for nums in mun:
        if nums == 0:
            s += 1
        else:
            s = 0
        
        h = max(s, h)
        
    return h
        
print(max_ones([1,1,0,1,1,1,1,0,0]))         