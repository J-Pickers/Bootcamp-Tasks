sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace "!" with " "
spaced_sentence = sentence.replace("!"," ")

# Convert to upper case
caps_sentence = spaced_sentence.upper()

# Reverse the sentence 
rev_sentence = spaced_sentence[::-1]

# Print each new sentence - using f-string and triple quotes to reduce number of print statements needed
print(f"""{spaced_sentence}
      
{caps_sentence}

{rev_sentence}
""")