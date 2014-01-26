# defines no. of cars
cars = 100
# defines space in car, which is equal to no. of seats
space_in_car = 4.0
# defines no. of drivers that exist
drivers = 30
# defines no. of passengers
passengers = 90
# defines no. of cars that aren't driven (existing pool of cars - cars being driven)
cars_not_driven = cars - drivers
# defines cars driven which is equal to no. of drivers
cars_driven = drivers 
#defines carpool capacity of driving pool (cars on road [drivers] * space avail [seats]
carpool_capacity = cars_driven * space_in_car
#defines avg. people being driven which is equal to poeple over cars on the road 
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"