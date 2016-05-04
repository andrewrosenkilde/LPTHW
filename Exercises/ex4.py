#defines the variable "cars".
cars = 100
# defines the variable space_in_a_car
space_in_a_car = 4
# defines the variable drivers
drivers = 30
#defines the variable passengers
passengers = 90
#defines the variable cars_not_driven as the math of
# cars - drivers
cars_not_driven = cars - drivers
# defines the variable cars_driven as the value of
# the variable drivers
cars_driven = drivers
# defines carpool_capacity as the math of
# cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# defines the variable average_passengers_per_car
# as the math of passengers / cars_driven
average_passengers_per_car = passengers / cars_driven

# prints each variable in a string
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drill 0's error means that the author
# did not define the variable car_pool_capacity
# and then called for the variable on line 8 when it
# did not exist.

# Study Drill 1:
# It is not necessary, you get 120 instead of 120.0
# if you use a whole number instead of a float.

#CSQ 3:
print "Hey %s there." % "you"
# vs:
print "Hey", "you", "there."