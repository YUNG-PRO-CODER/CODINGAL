print("================================")
print("TARGET TRACKER LAB")
print("================================")

numbers = [-4, 6, 2, 0, 0, 1, 1]

print("Full Array:", numbers)

index = 2
left_slice = numbers[:index]
right_slice = numbers[index + 1:]

print("Left of index", index, ":", left_slice)
print("Right of index", index, ":", right_slice)
print("Left Sum:", sum(left_slice))
print("Right Sum:", sum(right_slice))


for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])
    print("Index", i, "-> Left Sum:", left_sum, "| Right Sum:", right_sum)


for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])

    if left_sum == right_sum:
        print("Equilibrium found at index:", i)
        print("Element:", numbers[i])

values = [3, 6, 2, 2, 4, 1]

print("Array:", values)

window_sum = 0

for i in range(len(values)):
    window_sum = window_sum + values[i]
    print("Window from index 0 to", i, ":", values[:i + 1], "| Sum:", window_sum)

target = 10

print("Target Sum:", target)

found = False

for start in range(len(values)):
    current_sum = 0

    for end in range(start, len(values)):
        current_sum = current_sum + values[end]

        if current_sum == target:
            print("Target subarray found:", values[start:end + 1])
            print("Start Index:", start)
            print("End Index:", end)
            found = True

if found == False:
    print("No subarray found with target sum.")