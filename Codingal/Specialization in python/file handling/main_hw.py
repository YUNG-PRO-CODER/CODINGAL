"""In this assignment, students will build a Shopping List Manager using Python file handling. 
They will create a text file, write a shopping list into it, read the complete file, append new items, and read the updated file line by line. 
The activity helps students understand how programs store and reuse information using files."""

gaming_list = open("gaming_list.txt", "r")
print(gaming_list.read())
gaming_list.close()

gaming_list = open("gaming_list.txt", "a")
print(gaming_list.write("""
1.CPU: AMD Ryzen 9 9950X3D
2.GPU: Nvidia RTX 5090
3.RAM: 64GB DDR5
4.Storage: 8TB SSD
5.Cooling: Custom chassis, 200W CPU / 600W GPU continuous draw
6.Weight: 76.1 lbs
"""))
gaming_list.close()

gaming_list = open("gaming_list.txt", "r")
num_of_components = gaming_list.readlines()
num = len(num_of_components)
print("\n \t")
print("Number of components ", num)

gaming_list = open("gaming_list.txt", "a")
print("\n \t")
print(gaming_list.write("The best build ever in the whole world"))
gaming_list.close()