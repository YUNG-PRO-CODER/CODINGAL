# reversing numbers

def reversing(n, rev=0):
    if n == 0:
        return rev

    p = n % 10
    rev = rev * 10 + p

    return reversing(n // 10, rev)


n = int(input("Type a number: "))

print(reversing(n))

#armstrong number

def reversing_string(n):
    if n == "":
        return ""

    return reversing_string(n[1:]) + n[0]

n = input("Name: ")

print(reversing_string(n))

#power of four 4 

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
