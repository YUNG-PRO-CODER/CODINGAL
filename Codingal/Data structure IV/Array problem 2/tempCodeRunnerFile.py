def rainwater(n):
    bars = [0, n, 0, n]
    size = len(bars)
    
    left = [0] * size
    right = [0] * size
    
    left[0] = bars[0]
    
    for i in range(1, size):
        left[i] = max(left[i - 1], bars[i])
        
    right[size - 1] = bars[size - 1]
    
    for i in range(size - 2, -1, -1):
        right[i] = max(right[i + 1], bars[i])
        
    w = 0
    
    for i in range(size):
        w += min(left[i], right[i]) - bars[i]
        
    return w

print(rainwater(3))