print("================================")
print("FLIP IT WITH RECURSION")
print("================================")


number = 4827
temp = number

print("Original Number:", number)

while temp > 0:
    last_digit = temp % 10
    remaining_number = temp // 10

    print("Last Digit:", last_digit, "| Remaining Number:", remaining_number)

    temp = remaining_number



def count_digits(num):
    if num < 10:
        return 1
    return 1 + count_digits(num // 10)


def reverse_number(num):
    if num < 10:
        return num

    last_digit = num % 10
    remaining_number = num // 10
    digits_left = count_digits(remaining_number)

    return last_digit * (10 ** digits_left) + reverse_number(remaining_number)


num = 4827
print("Original Number:", num)
print("Reversed Number:", reverse_number(num))



def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


word = "CODING"
print("Original String:", word)
print("Reversed String:", reverse_string(word))


def is_power_of_4(num):
    if num <= 0:
        return False

    if num == 1:
        return True

    if num % 4 != 0:
        return False

    return is_power_of_4(num // 4)

numbers = [1, 4, 8, 16, 20, 64, 100, 256]

for value in numbers:
    print(value, "is power of 4:", is_power_of_4(value))


print("Stopping condition 1: num <= 0 stops invalid power checks.")
print("Stopping condition 2: num == 1 confirms the number is a power of 4.")
print("String recursion also stops when the string length is 0 or 1.")


