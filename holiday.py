destinations = ["Madrid", "Paris", "Berlin", "Rome", "Tenerife",
                "Tokyo", "Miami", "Sydney"]
dest_string = " - ".join(destinations)

print("Hello there! Please enter the required information when "
      "prompted. When entering a destination, please choose from "
      "the following selection: "
      )
print(f"\n{dest_string}")

# This while loop will ensure that a valid destination is entered
# before continuing with the rest of the program
while True:
    city_flight = input("\nWhich city will you fly to?: ").capitalize()
    if city_flight not in destinations:
        print("Please enter a valid destination!")
        continue
    break

num_nights = int(input("\nHow may nights are you staying?: "))
rental_days = int(input("\nHow many days will you be hiring a car?: "))

# I decided to get a bit more creative and make the hotel price
# dependant on the destination. These if/elif statements
# facilitate this.
def hotel_cost(nights):
    if city_flight in ("Madrid","Tenerife"):
        price_per_night = 109.99
    elif city_flight in ("Paris","Berlin"):
        price_per_night = 239.99
    elif city_flight in ("Rome","Sydney"):
        price_per_night = 189.99
    elif city_flight in ("Tokyo","Miami"):
        price_per_night = 214.99
    return round((price_per_night * nights), 2)
    # Rounded the output to remove recurring decimals

# These if/elif statements provide effectively the same function, but
# for flight prices
def plane_cost(city):
    if city == "Madrid":
        return 219.99
    if city == "Paris":
        return 224.45
    if city == "Berlin":
        return 249.99
    if city == "Rome":
        return 274.99
    if city == "Tenerife":
        return 289.55
    if city == "Tokyo":
        return 379.99
    if city == "Miami":
        return 390.67
    if city == "Sydney":
        return 449.99

# I decided the car rental should stay the same regardless
# (Call it a company guarantee!)
def car_rental(days):
    return days * 80

# This function sums the total of the three previous functions
# when fed them
def holiday_cost(nights, city, rental):
    t = hotel_cost(nights) + plane_cost(city) + car_rental(rental)
    return round(t,2)


# Calls all functions within an f-string on output to user
print(f"\nYour flights to {city_flight} will cost "
      f"£{plane_cost(city_flight)}.\nTo stay for {num_nights} nights, "
      f"the hotel will cost £{hotel_cost(num_nights)}.\nTo rent a car "
      f"for {rental_days} days will cost £{car_rental(rental_days)}. "
      f"\n\nIn total, your holiday package will cost "
      f"£{holiday_cost(num_nights,city_flight,rental_days)}.")
