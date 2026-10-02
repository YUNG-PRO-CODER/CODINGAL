def q(n):
    if n == 1:
        return 1
    else:
        return q(2) + q(2)