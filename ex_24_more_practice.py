print "Let's practice everything"
print "You'd need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

print " --------------------- "
print poem
print " --------------------- "


five = 10 - 2 + 3 - 6;
print "This should be five: ", five


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


#we assign a value to our variable start_point which we pass as a argument in function called secret_formula
start_point = 10000
#we create 3 variables which we pass to our function
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars and %d crates." %(beans, jars, crates)

#we assign new parameter to pass to our function by dividing it by 10
start_point = start_point / 10

print "We can also do this way: "
print "We'd have %d beans, %d jars and %d crates." % secret_formula(start_point)
