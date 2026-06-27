file = open("physics_notes.txt", "r", encoding="utf-8")
print(file.read(),"\n \t")
file.close()

file = open("physics_notes.txt", "r", encoding="utf-8")
for files in file:
    print(files.strip(),"\n \t")
file.close()

file = open("physics_notes.txt", "r", encoding="utf-8")
char = file.read(123456)
print(char,"\n \t")
file.close()

wrd = input("Skipping lines starting with -> ")

file = open("physics_notes.txt", "r", encoding="utf-8")
for line in file:
    if line.lower().startswith(wrd):
        print("Skipped -> ", line.strip())
    else:
        print("Kept -> ", line.strip())
file.close()

