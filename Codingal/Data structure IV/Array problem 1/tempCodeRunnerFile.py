def op(n):
    for i in range(0, 6, n):
        arr = [2,4,6,8,10,12]
        arr[i:i+n] = arr[i:i+n][::-1]
        return arr
    
print(op(3))