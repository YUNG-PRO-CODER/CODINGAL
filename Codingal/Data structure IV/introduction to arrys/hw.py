import array

numbers = array.array('i', [10, 20, 30, 40, 50])

def mean(arr):
    total = 0

    for num in arr:
        total += num

    return float(total / len(arr))


def median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)

    if n % 2 != 0:
        return float(sorted_arr[n // 2])
    else:
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]

        return float((mid1 + mid2) / 2)


print("Array:", numbers)
print("Size:", len(numbers))

print("Mean:", mean(numbers))
print("Median:", median(numbers))


#MinArrayMax

import array as arr

def MaxArrayMin(a):
    print("Max:", max(a))
    print("Min:", min(a))

a = arr.array('i', [2, 4, 6 , 1, 8, 3])

MaxArrayMin(a)

#Second largest element

import array as arr

z = arr.array('i', [2, 4, 6, 7 , 1, 8, 3])
z = sorted(z)

print(z[-2])
