# SWITCH BIT MONITOR
switch_names = [
    "Living Room Light",
    "Fan",
    "Air Conditioner",
    "Door Lock",
    "Garden Light",
    "Security Camera"
]


def show_bits(number):
    return bin(number)[2:]

def set_and_zero_bits(switch_value):

    binary_value = show_bits(switch_value)
    set_bits = binary_value.count("1")
    zero_bits = binary_value.count("0")

    print("\nPART 1: Set Bits and Zero Bits")
    print("Set Bits / ON Switches:", set_bits)
    print("Zero Bits / OFF Switches:", zero_bits)

    return set_bits, zero_bits


def count_set_bits(switch_value):

    count = 0
    temp = switch_value
    while temp > 0:
        if temp & 1:
            count = count + 1

        temp = temp >> 1

    print("\nPART 2: Counting Set Bits")
    print("Number of ON switches:", count)

    return count


def first_set_bit(switch_value):

    if switch_value == 0:
        print("\nPART 3: The First Set Bit")
        print("No switches are ON.")
        return -1

    position = 0
    temp = switch_value
    while temp > 0:
        
        if temp & 1:
            break

        position = position + 1
        temp = temp >> 1

    print("\nPART 3: The First Set Bit")
    print("First ON switch is at Bit:", position)
    print("Switch:", switch_names[position])

    return position


def build_bit_masks():

    print("\nPART 4: Building Bit Masks")

    for i in range(6):

        mask = 1 << i

        print(
            "Bit", i,
            "Mask:", mask,
            "Binary:", show_bits(mask)
        )


def check_nth_bits(switch_value):

    print("\nPART 5: Check if the Nth Bit is Set")
    for i in range(6):
        mask = 1 << i

        if switch_value & mask:
            print(
                "Bit", i,
                "-", switch_names[i],
                "is ON"
                )
        else:
            print(
                "Bit", i,
                "-", switch_names[i],
                "is OFF"
            )


def summary(
    switch_value,
    count,
    first_position
):

    print("\n================================")
    print("SMART SWITCH SUMMARY")
    print("================================")
    print("Switch Value:", switch_value)
    print("Binary Form:", show_bits(switch_value))
    print("Total ON Switches:", count)

    if first_position != -1:
        print("First ON Switch Bit:", first_position)
        print("First ON Switch:", switch_names[first_position])
    else:
        print("First ON Switch: None")
    print("================================")


print("================================")
print("MY SMART SWITCH BIT MONITOR")
print("================================")



try:

    switch_value = int(
        input("Enter switch value: ")
        )

    if switch_value < 0:
        print("Please enter a positive number.")
    else:
        print(
            "\nSwitch Value:",
            switch_value
        )
        print(
            "Binary Form:",
            show_bits(switch_value)
        )


        set_bits, zero_bits = set_and_zero_bits(switch_value)
        count = count_set_bits(switch_value)
        first_position = first_set_bit(switch_value)
        build_bit_masks()
        check_nth_bits(switch_value)
        summary(switch_value, count, first_position)
        
except ValueError:
    print("Invalid input! Please enter a number.")