print "How old are you?",
age = int(raw_input())
print "How tall are you?"
height = raw_input()
print "How much do you weight?"
weight = input()


print "So, you're %d old, %r tall and %r heavy." % (age, height, weight)
print "So, you're {} old, {} tall and {} heavy." .format(age, height, weight)