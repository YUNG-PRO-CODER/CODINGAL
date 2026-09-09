def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input(f"What number would u like to get the factorial of: ", ))
print(factorial(n))
