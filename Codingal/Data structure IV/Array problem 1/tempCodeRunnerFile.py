arr = [1,2,3,4,5]

n = 900

n = n % len(arr)

w = arr[n:] + arr[:n]

print(w)