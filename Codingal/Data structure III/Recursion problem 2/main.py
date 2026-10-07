#climbing stairs

def ways(stairs):
    if stairs == 0:
        return 1
    if stairs < 0:
        return 0

    return ways(stairs - 1) + ways(stairs - 2)


stairs = int(input("Enter number of stairs: "))
print("Number of ways:", ways(stairs))

#problem paranthesis

# Balanced Parentheses Problem

def count_paren(n, l=0, r=0):
    
    if l == n and r == n:
        return 1

    total = 0

    if l < n:
        total += count_paren(n, l + 1, r)

    if l > r:
        total += count_paren(n, l, r + 1)

    return total


n = int(input("Enter number of pairs: "))
print("Number of valid arrangements:", count_paren(n))


