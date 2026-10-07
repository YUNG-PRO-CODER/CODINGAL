def ways(stairs):
    if stairs == 0:
        return 1
    if stairs < 0:
        return 0

    return ways(stairs - 1) + ways(stairs - 2)


stairs = int(input("Enter number of stairs: "))
print("Number of ways:", ways(stairs))