# This program intends to tell the user what note is a certain amount
# of half-steps higher than their start note.
# I have pre-assigned values for both to showcase a runtime error


scale = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"]

start = ab # Compilation error - this should be enclosed in quotes
start_cap = start.capitalize()

if start_cap in scale:
    step = 5
    start_index = scale.index(start_cap)
    end_index = start_index - step # This is a logical error, the operator should be +
    end_note = scale{end_index} # Compilation error - these braces should be square

    print(f"{end_note} is {step} half-steps higher than {start_cap}.")

else:
    print("That note is not available!")

# If the logical and compilation errors were to be fixed, this program
# would experience a runtime error on line 15 as it attempts to
# reference an index which is out of range.

