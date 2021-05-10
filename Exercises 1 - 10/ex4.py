# Notes:
# Study drill 1 - The error occured because the variable "carpool_capacity"
# was improperly spelled when referenced in line 8, adding an underscore
# where it was not already present: "car_pool_capacity".
#
# Study drill 2 - Only change when inputting "4" instead of "4.0" is that
# carpool_capacity no longer outputs as a floating point number.
#
# Study drill 3 - Notation complete.
#
# Study drill 4 - Variables inputted individually, equation successful.



# Defines the number of cars
cars = 100
# Defines the maximum seating for passengers
space_in_a_car = 4
# Defines the number of drivers
drivers = 30
# Defines the number of passengers
passengers = 90
# Equates the number of undriven cars by subtracting the number of drivers
# from the number of cars
cars_not_driven = cars - drivers
# Narrows the number of usable cars to only those occupied by a driver
cars_driven = drivers
# Equates the amount of seats available for use, including drivers, of only
# those cars operated by a driver
carpool_capacity = cars_driven * space_in_a_car
# Divides the amount of passengers among cars operated by a driver
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
