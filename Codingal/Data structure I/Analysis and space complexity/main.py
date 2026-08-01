"""linear search"""
marks = [91, 74, 86, 59, 97, 68, 81, 93, 77, 62,55, 89, 71, 84, 66, 79, 95, 58, 73, 87,69, 82, 76, 90, 64, 53, 99, 88, 61, 78,
72, 85, 57, 92, 80, 67, 94, 75, 60, 83,
56, 70, 96, 63, 54, 65, 98, 51, 50, 47]


marks.sort()

print("print the sorted marks \n \t")
print(marks, "\n \t")

n = len(marks)
target = 98

s = 0

for i in range(n):
    s += 1
    if marks[i] == target:
        print("mark found ", target)
        print("Index ", i, " steps ", s, "O(n)")
        break
print()    

"""binary search"""



