def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, "A", "B", "C")

#phone keypad problem

keypad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def keypad_combinations(s, index=0, result=""):
    if index == len(s):
        print(result)
        return

    for ch in keypad[s[index]]:
        keypad_combinations(s, index + 1, result + ch)


n = input("Enter number: ")

keypad_combinations(n)
