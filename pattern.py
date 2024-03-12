row = 0

for i in range(1, 10): # Used range func to iterate 9 times
    if i < 6:
        row += 1 # Increments total "*" printed per line up to 5
    else:
        row -=1 # Decrements total "*" per line back down from 5
    print("*" * row)
