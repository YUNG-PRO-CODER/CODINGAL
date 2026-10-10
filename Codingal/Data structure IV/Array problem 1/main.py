x = [1, 2, 3, 4, 5, 6]

s = 0
j = len(x) - 1

while s <= j:
    x[s], x[j] = x[j], x[s]
    s = s + 1
    j = j + 1
    
print(x)


#left rotate

arr = [1,2,3,4,5]

n = 3

n = n % len(arr)
w = arr[n:] + arr[:n]
print(w)

#reversing in group

def op(n):
    for i in range(0, 6, n):
        arr = [2,4,6,8,10,12]
        arr[i:i+n] = arr[i:i+n][::-1]
        return arr
    
print(op(3))
    
