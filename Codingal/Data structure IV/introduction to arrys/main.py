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