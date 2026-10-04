 lis = [100, 200, 300, 400, 500]

    high = lis[0]
    low = lis[0]

    if len(lis) == 1:
        return lis[0]

    if lis[0] <= lis[1]:
        return lis[0] + m(lis[1:])