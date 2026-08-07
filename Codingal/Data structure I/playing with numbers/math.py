"""palindrome code"""

num = int(input("Type ur numbers: "))

ori_num = num
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10
    
if ori_num == rev_num:
    print("its a palindrome number : ", ori_num)
else:
    print("its not a palindrome number : ", ori_num)
    
    
