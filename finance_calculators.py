import math

# Print opening instructions
print("investment - to calculate the amount of interest you'll earn "
      "on your investment bond\nbond       - to calculate the amount "
      "you'll have to pay on a home loan")

# Receive preffered program
user_choice = input("\nEnter either \'investment\' or \'bond\' from "
                    "the menu above to proceed: ")

# Convert all entries to lower case to allow for multiple input formats
user_choice_lowered = user_choice.lower()

# Check if investment option has been selected
if user_choice_lowered == "investment":
    # Receive relevant user inputs
    deposit       = float(input("\nPlease enter your deposit "
                                "amount: "))
    interest_rate = float(input("\nPlease enter your interest "
                                "rate: "))
    years         = int(input("\nPlease enter how many years you "
                              "are investing for: "))
    interest      = input("\nWill you be using simple or compound "
                          "interest?: ")

    interest      = interest.lower()
    one_percent   = interest_rate/100     # Needed for next formula

    # Nested if statement to check for simple vs compound interest
    if interest == "simple":
        total = round((deposit *(1 + one_percent*years)), 2)
        print(f"\nAfter {years} years at {interest_rate}% simple "
              f"interest, \nyour investment of £{deposit} will "
              f"mature to £{total}!")

    elif interest == "compound":
        total = round((deposit * math.pow((1+one_percent),years)), 2)
        print(f"\nAfter {years} years at {interest_rate}% compound "
              f"interest, \nyour investment of £{deposit} will "
              f"mature to £{total}!")

    else:
        print("\nYour selection was not valid!")

# Check if bond option has been selected
elif user_choice_lowered == "bond":

    # Receive user inputs
    present_value  = float(input("\nPlease enter the current value of "
                                 "the house: "))
    interest_rate  = float(input("\nPlease enter the interest rate: "))
    months         = int(input("\nPlease enter how many months you "
                               "will be repaying for: "))

    monthly_rate = (interest_rate/100) / 12
    repayment    = ((monthly_rate * present_value)
                    /(1 - (1 + monthly_rate)**(-months)))

    print(f"\nFor a house with value of £{present_value}, "
          f"being paid over {months} months, at {interest_rate}% "
          f"interest, your repayments will be £{round(repayment, 2)}"
          f" per month.")

else:
    print("\nYour selection was not valid!")
