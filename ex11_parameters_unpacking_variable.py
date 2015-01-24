from sys import argv


script, first, second, third = argv

first = raw_input('What is your name? ')

print "The script is called: ", script
print "The first variable is: ", first
print "The second variable is: %s " % second
print "The third variable is:", third

print first + ' likes ' + second
r = raw_input("How are you? ")
print first + ' is feeling ' + str(r)