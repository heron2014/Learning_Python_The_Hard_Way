people = 30
cars = 40
trucks = 15


if cars > people:
    print 'We should take a car'
elif cars < people:
    print 'We should not take a car'
else:
    print 'We ca\'t decide'

#if cars are greater than people and trucks are less then cars(if this condition is true) print We should not take a car
#or if cars are less than people is true print We should take a car, if none of these condition are true
# return we cant decide.
if cars > people and trucks < cars:
    print 'We should not take a car'
elif cars < people:
    print 'We should take a car'
else:
    print 'We ca\'t decide'

if trucks > cars:
    print "That's too many trucks"
elif trucks < cars:
    print "Maybe we could take a truck"
else:
    print "We still can't decide"


if people > trucks:
    print "All right, lets just take the trucks"
else:
    print "Fine lets stay home then"
