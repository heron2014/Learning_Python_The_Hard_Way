# -*- coding: utf-8 -*-
my_name = 'Anita'
my_age = 30
my_height = 165
my_weight = 70
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blond'

print "Let's talk about %s." % my_name
print "She's %d cm tall." % my_height
print "She's %d pounds heady" % my_weight
print "Actually that's not heavy."
print "She's got %s and %s." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee" % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight )