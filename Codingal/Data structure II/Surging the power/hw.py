def bit_trick(n):
    print("\nPART 1: The n & (n-1) Trick")
    print("n       =",n,"->",bin(n))
    print("n - 1   =",n-1,"->",bin(n-1))
    print("n&(n-1) =",n&(n-1),"->",bin(n&(n-1)))
    print("This trick removes the rightmost set bit.")


def is_power_of_2(num):
    return num>0 and (num&(num-1))==0


def power_of_2(numbers):
    print("\nPART 2: Power of 2 Check")
    for num in numbers:
        print(num,"->",bin(num),"->",is_power_of_2(num))


def is_power_of_4(num):
    if not is_power_of_2(num):
        return False
    position=0

    while num>1:
        num=num>>1
        position+=1
    return position%2==0


def power_of_4(numbers):
    print("\nPART 3: Power of 4 Check")
    for num in numbers:
        print(num,"->",is_power_of_4(num))


def is_power_of_8(num):
    if not is_power_of_2(num):
        return False
    position=0
    
    while num>1:
        num=num>>1
        position+=1
    return position%3==0


def power_of_8(numbers):
    print("\nPART 4: Power of 8 Check")
    for num in numbers:
        print(num,"->",is_power_of_8(num))


def binary_power(base,exponent):
    answer=1
    while exponent>0:
        if exponent&1:
            answer*=base

        base*=base
        exponent=exponent>>1
    return answer


def show_binary_power():
    
    print("\nPART 5: Binary Exponentiation")
    base1=int(input("Enter base 1: "))
    exponent1=int(input("Enter exponent 1: "))
    base2=int(input("Enter base 2: "))
    exponent2=int(input("Enter exponent 2: "))
    base3=int(input("Enter base 3: "))
    exponent3=int(input("Enter exponent 3: "))

    print(base1,"^",exponent1,"=",binary_power(base1,exponent1))
    print(base2,"^",exponent2,"=",binary_power(base2,exponent2))
    print(base3,"^",exponent3,"=",binary_power(base3,exponent3))


def summary():
    print("\n================================")
    print("POWER SCANNER SUMMARY")
    print("================================")
    print("Power of 2: only one bit is set.")
    print("Power of 4: set-bit position is even.")
    print("Power of 8: set-bit position is divisible by 3.")
    print("Binary exponentiation calculates powers quickly.")
    print("================================")


print("================================")
print("POWER OF TWO SCANNER")
print("================================")

try:
    n=int(input("Enter n: "))
    numbers=list(
        map(int,input("Enter numbers separated by spaces: ").split())
    )

    bit_trick(n)
    power_of_2(numbers)
    power_of_4(numbers)
    power_of_8(numbers)
    show_binary_power()
    summary()

except ValueError:
    print("Invalid input! Please enter numbers only.")