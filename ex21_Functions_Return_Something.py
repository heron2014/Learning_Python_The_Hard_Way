def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return  a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Lets do some math with just our functions!\n\n"

age = add(30, 5)
height = subtract(200, 59)
weight = multiply(300, 34)
iq = divide(456, 78)

print "\nAge: %d \n Height: %d \n Weight: %d \n Iq: %d \n" % (age, height, weight, iq)

#A puzzle

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand? "