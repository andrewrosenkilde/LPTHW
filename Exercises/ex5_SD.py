# SD1
name = "Zed A. Shaw"
age = 35 #not a lie
height = 74 # inches
weight = 180 #lbs
eyes = "Blue"
teeth = "White"
hair = "Brown"

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's god %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

# SD2
i = "Blue"
print "This is %s" % (i)

# SD4

_weight = 180.0 #pounds
_lbs_to_kilos_conversion_factor = 2.2 #lbs in a kilo
_weight_in_kilos = _weight / _lbs_to_kilos_conversion_factor
print _weight
print "%d pounds in kg is %d." % (_weight, _weight_in_kilos)
