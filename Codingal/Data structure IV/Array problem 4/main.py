def eq_mid(n):
    arr = [1] * n + [0] + [1] * n
    size = len(arr)

    for i in range(size):
        left_sum = 0
        right_sum = 0

        for j in range(i):
            left_sum += arr[j]

        for j in range(i + 1, size):
            right_sum += arr[j]

        if left_sum == right_sum:
            return i

    return -1


n = int(input("Enter a number ( 5 or 6): "))
guess = input("Guess the equilibrium index: ")

result = eq_mid(n)

print("Actual result:", result)
print()
print("Your guess:", guess)