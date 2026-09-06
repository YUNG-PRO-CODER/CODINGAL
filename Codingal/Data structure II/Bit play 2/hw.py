def xor_identity(a,b):
    print("\nPART 1: XOR Identity and Equality")
    print("a =",a)
    print("b =",b)
    print("a ^ a =",a^a)
    print("a ^ 0 =",a^0)

    if (a^b)==0:
        print("Both numbers are equal")
    else:
        print("Both numbers are different")


def xor_cancellation(clues):
    xor_result=0

    for clue in clues:
        xor_result^=clue

    print("\nPART 2: XOR Cancellation")
    print("Clues:",clues)
    print("Final XOR Result:",xor_result)
    print("Remaining clue:",xor_result)

    return xor_result


def one_odd_number(numbers):
    odd_number=0

    for number in numbers:
        odd_number^=number

    print("\nPART 3: One Odd-Occurring Number")
    print("Numbers:",numbers)
    print("Odd-occurring number:",odd_number)

    return odd_number


def two_odd_numbers(numbers):
    xor_of_two=0

    for number in numbers:
        xor_of_two^=number

    print("\nPART 4: XOR of Two Odd-Occurring Numbers")
    print("Numbers:",numbers)
    print("XOR of two odd-occurring numbers:",xor_of_two)

    return xor_of_two


def split_two_odd_numbers(numbers,xor_of_two):
    rightmost_set_bit=xor_of_two&-xor_of_two
    first_odd=0
    second_odd=0

    for number in numbers:
        if number&rightmost_set_bit:
            first_odd^=number
        else:
            second_odd^=number

    print("\nPART 5: Splitting by the Rightmost Set Bit")
    print("Rightmost set bit:",rightmost_set_bit)
    print("First odd-occurring number:",first_odd)
    print("Second odd-occurring number:",second_odd)

    return first_odd,second_odd


def summary(odd_number,first_odd,second_odd):
    print("\n================================")
    print("BINARY CLUE INVESTIGATION SUMMARY")
    print("================================")
    print("XOR Identity: a ^ a = 0")
    print("XOR with zero: a ^ 0 = a")
    print("XOR Cancellation removes repeated pairs")
    print("One odd-occurring number found:",odd_number)
    print("Two odd-occurring numbers found:",first_odd,"and",second_odd)
    print("================================")


print("================================")
print("BINARY CLUE INVESTIGATOR")
print("================================")

try:
    a=int(input("\nEnter number a: "))
    b=int(input("Enter number b: "))

    clues=list(map(int,input("\nEnter clues separated by spaces: ").split()))
    numbers=list(map(int,input("Enter numbers for odd-occurring test: ").split()))
    pair_numbers=list(map(int,input("Enter numbers with TWO odd-occurring values: ").split()))

    xor_identity(a,b)
    xor_cancellation(clues)
    odd_number=one_odd_number(numbers)
    xor_of_two=two_odd_numbers(pair_numbers)
    first_odd,second_odd=split_two_odd_numbers(pair_numbers,xor_of_two)

    summary(odd_number,first_odd,second_odd)

except ValueError:
    print("\nInvalid input! Please enter numbers only.")