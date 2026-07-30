"""Suppose a plant has height 1.75 feet and it grows by 0.5 feet each
month.
Find the height after 7 months"""


height = 1.75
growth_spurt = 0.5
month = 7

def pattern() -> float:
    return height + (growth_spurt * month)
    
def loop_pattern() -> float:
    a = 0
    
    for _ in range(month):
        a += growth_spurt
    return height + a

def nested_loop() -> float:
    
    z = 0
    
    for _ in range(month):
        for _ in range(1):
            z += growth_spurt
    return height + z
    
print(pattern(), "\n")    
print(loop_pattern(), "\n")
print(nested_loop(), "\n")