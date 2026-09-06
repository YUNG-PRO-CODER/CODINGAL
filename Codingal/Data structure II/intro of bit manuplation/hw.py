
# BIT SCANNER


def bits(number, width=4):
    return format(number & ((1 << width) - 1), f"0{width}b")


def show_binary(secret_code, access_key):
    print("\nPART 1: Bits and Binary")
    print("Secret Code Binary:", bits(secret_code))
    print("Access Key Binary:", bits(access_key))

def and_or(secret_code, access_key):
    and_result = secret_code & access_key
    or_result = secret_code | access_key

    print("\nPART 2: AND and OR")
    print("AND Result:", and_result, "Binary:", bits(and_result))
    print("OR Result:", or_result, "Binary:", bits(or_result))

    return and_result, or_result

def not_xor(secret_code, access_key):
    not_result = (~secret_code) & 0b1111
    xor_result = secret_code ^ access_key

    print("\nPART 3: NOT and XOR")
    print("NOT Result:", not_result, "Binary:", bits(not_result))
    print("XOR Result:", xor_result, "Binary:", bits(xor_result))

    return not_result, xor_result

def shifts(secret_code):
    left_shift = secret_code << 1
    right_shift = secret_code >> 1

    print("\nPART 4: Left Shift and Right Shift")
    print("Left Shift:", left_shift, "Binary:", bits(left_shift, 5))
    print("Right Shift:", right_shift, "Binary:", bits(right_shift))

    return left_shift, right_shift

def odd_even_xor(secret_code):
    xor_check = secret_code ^ 1

    print("\nPART 5: Odd or Even with XOR")
    print("Secret Code XOR 1:", xor_check)

    if xor_check == secret_code - 1:
        print("Secret Code is Odd")
        return "Odd"
    else:
        print("Secret Code is Even")
        return "Even"

def count_bits(secret_code):
    bit_count = secret_code.bit_count()

    print("\nPART 6: Counting Bits")
    print("Number of 1 bits:", bit_count)

    return bit_count

def summary(secret_code, access_key, and_result, or_result,
            not_result, xor_result, left_shift, right_shift, bit_count):

    print("\n================================")
    print("SECRET CODE SCAN SUMMARY")
    print("================================")

    print("Secret Code:", secret_code)
    print("Binary:", bits(secret_code))

    print("Access Key:", access_key)
    print("Binary:", bits(access_key))

    print("AND:", and_result)
    print("OR:", or_result)
    print("NOT:", not_result)
    print("XOR:", xor_result)
    print("Left Shift:", left_shift)
    print("Right Shift:", right_shift)
    print("1 Bits Count:", bit_count)

    print("================================")

print("================================")
print("MY SECRET CODE BIT SCANNER")
print("================================")



try:
    secret_code = int(input("Enter your secret code: "))
    access_key = int(input("Enter your access key: "))

    if secret_code < 0 or access_key < 0:
        print("Please enter positive numbers.")

    else:

        print("\nSecret Code:", secret_code)
        print("Binary:", bits(secret_code))

        print("Access Key:", access_key)
        print("Binary:", bits(access_key))


        show_binary(secret_code, access_key)
        and_result, or_result = and_or(secret_code, access_key)
        not_result, xor_result = not_xor(secret_code, access_key)
        left_shift, right_shift = shifts(secret_code)
        odd_even_xor(secret_code)
        bit_count = count_bits(secret_code)
        
        summary(
            secret_code,
            access_key,
            and_result,
            or_result,
            not_result,
            xor_result,
            left_shift,
            right_shift,
            bit_count
        )


except ValueError:
    print("Invalid input! Please enter numbers only.")