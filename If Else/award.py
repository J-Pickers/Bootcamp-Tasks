# Receive completion times (stored as float to allow for non-integer timings)
swimming_time = float(input("\nEnter your swimming time : "))
cycling_time = float(input("\nEnter your cycling time : "))
running_time = float(input("\nEnter your running time : "))

# Calculate total
total_time = swimming_time + cycling_time + running_time

# Determine the award
if total_time >= 111:
    award = "No award"
elif total_time < 111 and total_time >= 106:
    award = "Provincial Scroll"
elif total_time < 106 and total_time >= 101:
    award = "Provincial Half Colours"
else:
    award = "Provincial Colours"

# Print the award
print(f"\nYou received the award : {award}")
