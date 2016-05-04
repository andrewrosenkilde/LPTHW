import time
grav_scalr = 9.8
print "Welcome to the Physics Equation Machination!"
time.sleep(2)
print "This program will help you find the weight of something."
time.sleep(2)
mass_in_kg = input('Mass in kilograms: ')
weight_in_newtons = mass_in_kg * grav_scalr
print "Working..."
time.sleep(3)
print "The object weighs %s Newtons." % weight_in_newtons