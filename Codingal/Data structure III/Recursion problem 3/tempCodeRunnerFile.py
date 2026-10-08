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