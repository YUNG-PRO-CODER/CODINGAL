def  op(n):
    for i in range(0, 6, n):
        arr[i:i+n] = arr[i:i+n][::-1]
    return arr

c = input("Type your marks: ")
arr = [int(p) for p in c.split()]

print(op(3))