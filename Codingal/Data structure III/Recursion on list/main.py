def m(lis):

    high = lis[0]
    low = lis[0]

    if len(lis) == 1:
        return high, low

    if lis[0] <= lis[1]:
        high = lis[1]
        low = lis[0]
    else:
        high = lis[0]
        low = lis[1]

    next_high, next_low = m(lis[1:])

    high = max(high, next_high)
    low = min(low, next_low)

    return high, low


print(m([100, 200, 300, 400, 500]))