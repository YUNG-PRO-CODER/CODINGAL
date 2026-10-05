def power_of_four(n):
    if n == 1:
        return True

    if n <= 0 or n % 4 != 0:
        return False

    return power_of_four(n // 4)


n = int(input("Enter a number: "))

if power_of_four(n):
    print("Power of 4")
else:
    print("Not a power of 4")