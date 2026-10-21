print("================================")
print("BINARY STREAK TRACKER")
print("================================")
 
 
binary_scores = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print("Binary Array:", binary_scores)
print("This array contains only 0s and 1s.")
 
 
current_streak = 0
 
for score in binary_scores:
    if score == 1:
        current_streak = current_streak + 1
    else:
        current_streak = 0
 
    print("Score:", score, "| Current Streak:", current_streak)
 

 
current_streak = 0
best_streak = 0
 

 
for score in binary_scores:
    if score == 1:
        current_streak = current_streak + 1
        best_streak = max(best_streak, current_streak)
    else:
        current_streak = 0
 
print("Longest streak of 1s:", best_streak)
 
 
numbers = [0, 1, 0, 3, 12, 0, 5]
print("Original Array:", numbers)
 
write_pointer = 0
 
for read_pointer in range(len(numbers)):
    if numbers[read_pointer] != 0:
        numbers[write_pointer] = numbers[read_pointer]
        write_pointer = write_pointer + 1
 
print("After moving non-zero values forward:", numbers)
 
while write_pointer < len(numbers):
    numbers[write_pointer] = 0
    write_pointer = write_pointer + 1
 
print("Final Array after moving zeros to the end:", numbers)