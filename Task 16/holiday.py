#######################################FUNCTIONS##################################################


# Defines a function to calculate hotel cost based on the number of nights and city of the hotel.
def hotel_cost(num_nights, city_flight):
    # Creates dictionary to store hotel prices.
    hotel_prices = {
        "London": 180,
        "New York": 200,
        "Paris": 160,
        "Madrid": 140,
    }

    # Checks if the city is in the dictionary of 'hotel prices'.
    if city_flight in hotel_prices:
        # Calculates the cost per night and total hotel cost - then return value to 'total_cost'
        price_per_night = hotel_prices[city_flight]
        total_cost = num_nights * price_per_night
        return total_cost
    else:
        return None


# Defines a function to calculate plane cost based on the destination city.
def plane_cost(city_flight):
    # Creates dictionary to store flight prices for each city.
    flight_prices = {
        "London": 140,
        "New York": 160,
        "Paris": 200,
        "Madrid": 180,
    }

    # Checks if the city is in the dictionary of 'flight_prices'.
    if city_flight in flight_prices:
        return flight_prices[city_flight]
    else:
        return None


# Defines a function to calculate car rental cost based on the rental days and vehicle choice.
def car_rental(rental_days, vehicle):
    # Defines rental prices for different vehicle options.
    vehicle_options = {
        "Hatchback": 25,
        "Saloon": 50,
        "4x4": 75,
    }

    # Checks if the chosen vehicle is in the dictionary of 'vehicle_options.
    if vehicle in vehicle_options:
        # Calculates the cost per day and total car rental cost.
        price_per_day = vehicle_options[vehicle]
        total_cost = rental_days * price_per_day
        return total_cost
    else:
        return None


# Defines a function to calculate the total holiday cost.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    # Calculates the total cost by summing hotel, plane, and car rental costs.
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost


##############################################################################################


print("Welcome to the Holiday Cost Calculator!")

# Uses a while loop to repeatedly ask for the destination city until a valid one is provided.
while True:
    city_flight = input(
        "What city will you be flying to?: London, New York, Paris or Madrid: "
    ).capitalize()
    if city_flight in ["London", "New York", "Paris", "Madrid"]:
        break
    else:
        # Displays an error message for invalid input and continue the loop.
        print("Invalid input. Please choose a valid city from the list.")
        continue

# Uses a try-except block to handle input errors and ask for the number of nights.
while True:
    try:
        num_nights = int(input("How many nights will you be staying at the hotel?: "))
        break
    except ValueError:
        # Displays an error message for invalid input and continue the loop.
        print("Invalid input. Please enter a valid number of nights.")
        continue

# Uses a while loop to repeatedly ask for the rental vehicle until a valid one is provided.
while True:
    vehicle = input("Choose a rental vehicle (Hatchback, Saloon or 4x4): ").capitalize()
    if vehicle in ["Hatchback", "Saloon", "4x4"]:
        break
    else:
        # Displays an error message for invalid input and continue the loop.
        print("Invalid input. Please choose a valid rental vehicle.")
        continue

# Uses a try-except block to handle input errors and ask for the number of rental days.
while True:
    try:
        rental_days = int(input("How many days will you require a rental car?: "))
        break
    except ValueError:
        # Displays an error message for invalid input and continue the loop.
        print("Invalid input. Please enter a valid number of rental days.")
        continue

# Calculates the costs for hotel, plane, and car rental.
hotel_cost = hotel_cost(num_nights, city_flight)
plane_cost = plane_cost(city_flight)
car_rental = car_rental(rental_days, vehicle)

# Calculates the total holiday cost using the 'holiday_cost' function.
total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

# Displays the holiday details and total cost.
print(
    f"Your holiday details:\n"
    f"Destination: {city_flight}\n"
    f"Number of nights at the hotel: {num_nights}\n"
    f"Rental vehicle: {vehicle}\n"
    f"Number of rental days: {rental_days}\n"
    f"Total holiday cost: £{total_cost}"
)
