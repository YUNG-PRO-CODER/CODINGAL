#power set

def power_set(elements):
    n = len(elements)

    for mask in range(2 ** n):
        subset = []

        for i in range(n):
            if mask & (1 << i):
                subset.append(elements[i])

        print(f"{mask:0{n}b} -> {subset}")


power_set(['A', 'B', 'C'])


#bit probe

"""A Python program that uses (n >> j) & 1 to check whether a specific bit is ON or OFF 
and helps students understand how individual bit positions can be inspected."""


