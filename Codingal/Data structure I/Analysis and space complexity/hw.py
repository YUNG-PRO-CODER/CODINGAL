arr = list(range(1, 701))


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


try:
    i = int(input("Type your seat number: "))
    
    if 1 <= i <= 700:
        result = binary_search(arr, i)
        print("Seat found at index:", result)
    else:
        print("Seat number must be between 1 and 700.")

except ValueError:
    print("Try again.")