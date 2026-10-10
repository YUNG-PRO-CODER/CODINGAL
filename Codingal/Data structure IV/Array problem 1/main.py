x = [1, 2, 3, 4, 5, 6]

s = 0
j = len(x) - 1

while s <= j:
    x[s], x[j] = x[j], x[s]
    s = s + 1
    j = j + 1
    
print(x)