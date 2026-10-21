print("================================")
print("ARRAY ENERGY TRACKER")
print("================================")
 
energy_levels = [4, -6, 3, 5, -2, 7, -8, 4]
print("Full Array:", energy_levels)
 
print("Subarray [0:3]:", energy_levels[0:3], "Sum:", sum(energy_levels[0:3]))
print("Subarray [2:6]:", energy_levels[2:6], "Sum:", sum(energy_levels[2:6]))
print("Subarray [3:8]:", energy_levels[3:8], "Sum:", sum(energy_levels[3:8]))
 
running_sum = 0
 
for energy in energy_levels:
    running_sum = running_sum + energy
    print("Energy:", energy, "| Running Sum:", running_sum)
 
 
running_sum = 0
 
for energy in energy_levels:
    running_sum = running_sum + energy
 
    if running_sum < 0:
        print("Energy:", energy, "| Running Sum:", running_sum, "-> Reset to 0")
        running_sum = 0
    else:
        print("Energy:", energy, "| Running Sum:", running_sum)
 
 
running_sum = 0
max_so_far = 0
 
for energy in energy_levels:
    running_sum = running_sum + energy
 
    if running_sum < 0:
        running_sum = 0
 
    if running_sum > max_so_far:
        max_so_far = running_sum
 
    print("Energy:", energy, "| Running Sum:", running_sum, "| Max So Far:", max_so_far)
 
def kadane_algorithm(arr):
    running_sum = 0
    max_sum = arr[0]
 
    for num in arr:
        running_sum = running_sum + num
 
        if running_sum > max_sum:
            max_sum = running_sum
 
        if running_sum < 0:
            running_sum = 0
 
    return max_sum
 
 
best_energy = kadane_algorithm(energy_levels)
 
print("Energy Levels:", energy_levels)
print("Maximum Subarray Sum:", best_energy)
 
