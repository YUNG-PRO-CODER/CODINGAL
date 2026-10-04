def q(n):
    if n == 1:
        return 1
    return q(n - 1) + q(n - 1)

print(q(4))