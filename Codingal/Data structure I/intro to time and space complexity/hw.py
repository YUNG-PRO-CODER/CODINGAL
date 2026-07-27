"""If you have `800 and you save `250 every month, find the
amount you have after 6 months. Express this as
a linear pattern"""



month = 800
deposit = 250
x_month = 6



#first methord (formula methord)
#pattern = total money(800) + every_deposit(250)(number of months(x))
# time and complexity
#O(1) constant time 
def pattern():
    return month + (deposit * x_month)
  

#second methord (loop methord)   

"""
let savings be 0 

for _(null) in range(6(number of month))
    savings keeps on adding upto number of months which adds up with deposit
then return month the total added by savings from the above operation

time and complexity O(n)linear time

"""
 
def pattern_loop():
    savings = 0
    
    for _ in range(6):
        savings += deposit
    return month + savings

#thrid methord (nested loop)

"""
Let savings be 0

for each month in the range of 6 months
    for one iteration
        Add the monthly deposit to savings

Return month + savings
"""

def pattern_lop():
    savings = 0

    for _ in range(6):
        for _ in range(1):
            savings += deposit
    return month + savings
    
print(pattern(), "\n")
print(pattern_loop(), "\n")
print(pattern_lop(), "\n")