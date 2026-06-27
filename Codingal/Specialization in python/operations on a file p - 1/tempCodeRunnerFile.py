wrd = input("Skipping lines starting with -> ")

file = open("physics_notes.txt", "r", encoding="utf-8")
for line in file:
    if line.lower().startswith(wrd):
        print("Skipped -> ", line.strip())
    else:
        print("Kept -> ", line.strip())
file.close()