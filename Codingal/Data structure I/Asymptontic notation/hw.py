information = [
    {"Name": "Aarav", "id": 6673, "marks": 67.9},
    {"Name": "priya", "id": 9876, "marks": 99},
    {"Name": "devvidiya", "id": 3674, "marks": 0.1},
    {"Name": "pops", "id": 3842, "marks": 35},
]

"""finding the student"""

target = "devvidiya"
target1 = 3842
target2 = 99

for student in information:
    if student["Name"] == target:
        print("name found", student) 
        break
else:
    print("name not found")
    
for student1 in information:
    if student1["id"] == target1:
        print("id found ", student1)
        break
else:
    print("id not found")
    
for student2 in information:
    if student2["marks"] == target2:
        print("mark found ", student2)
        break

else:
    print("marks not found")