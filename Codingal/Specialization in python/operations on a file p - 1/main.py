n = int(input("How many characters to preview? "))
file = open("class_file.txt", "r", encoding="utf-8")
print(file.read(n))
file.close()
print()

file = open("class_file.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
print("Total lines:", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

wrds = input("Skip lines starting with ").strip().lower()
file = open("class_file.txt", "r", encoding="utf-8")

for line in file:
    if line.startswith(wrds):
        print("skip: ",line.strip())
    else:
        print("keep: ",line.strip())
file.close()
print()

