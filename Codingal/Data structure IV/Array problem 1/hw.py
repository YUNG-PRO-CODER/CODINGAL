"""In this assignment, you will build a Rotate My Scores program using Python arrays/lists. 
They will reverse scores using two pointers, reverse elements in fixed-size groups, 
perform left rotation by 1, perform left rotation by n, and find leaders in an array by scanning from the right side."""

scores  = [90,80,70,60,50]

s_1 = 0
e_1 = len(scores) - 1

while s_1 <= e_1:
    scores[s_1], scores[e_1] = scores[e_1], scores[s_1]
    s_1 = s_1 + 1
    e_1 = e_1 - 1
    
print(scores)

#reversing

score = input("Input scores: ")
sco = [int(c) for c in score.split()]


n = 3

n = n % len(sco)
b = sco[n:] + sco[:n]

print(b)


#reverse grouping

def op(n):
    for i in range(0, 6, n):
        arr[i:i+n] = arr[i:i+n][::-1]
    return arr

c = int(input("Type your marks: "))
arr = [int(p) for p in c.split()]

print(op)
    