# Review all the symbols I have used so far


print """\n
\t / -forward slash
\t \ -backslash
\t 1. print " whatever " - print anything which is between quotes
\t print "some stuff 5+ 6", 5+6
\t 2. math operations:
\t  % - modulo, division which returns reminder
\t >= - greater and equal, <= less and equal
\t to get floats you need to use dot notation: 4.0, 30.0 otherwise by default you get integers
\t \ - escape sequences
\t \\t - tab
\t \\n - newline
\t %s - string format , %s' converts a specified value to a string using the str() function.
\t %d - digits format conversion,
\t %r - raw conversion - s printing out the raw representation of what you typed,
\t usually used for debugging, will convert exact value from variable
\t \"\"\" - print statement on more than one lines
\t raw_input(prompt) - general input from the users, takes exactly what user types and paste it as a string
\t you can assign prompt to something like that: prompt = '> '
\t input() - expects a correct python statement
\t argv  - argument variable, holds the arguments you pass to your python script when u run it,
\t from sys import argv -sys- module, library
\t from sys import argv
\t script, first, second, third = argv - unpacks argv, so that rather than holding all the arguments it gets assigned
\t to 4 variables you can work with
\t import 'some modules' -import some prewritten modules
\n
\t t = open(filename) this one doesnt return content of the file, it makes a file_object which has other methods
\t to print out the content of the file which is read()
\t t.read() reads the contents of the file and the result you can assign to variable
\t close() - closes the file ex: f = open(filename, 'w') f.close()  w - means write mode  f.write('some string') - some
\t string wil be printed to the file or
\t f.write(variable), variable = 'some string' or raw_input('line1: ')
\t readline() - reads just one line of a text file
\t truncate() - empties the file.Watch out on this one! Make sure your file can be emptied!
\t from os.path import exists - 
"""

age = 3
age2 = '3'
print "some stuff 5+ 6", 5+6
print "Its fleece was white as %s." % 'snow'
print 'My niece is %d' % age
print 'My niece is: ', age
print 'My niece is ' + age2
print 'My niece is %r' % age2
print 'My niece age is {}'.format(age)
print 'My niece age is {} and also you can say she is {}'.format(age, age2)

x = "There are %d types of people\n\n" % 10
print x


#another approach
hilarius = 'lalalla'
joke_evaluation = "Isn't that joke so funny?! %r\n"

print joke_evaluation % hilarius

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
 #comma will make space between e and another e
print end1 + end2 + end3,
print end4 + end5 + end6
# if you omit comma the nest letter will start from next line
print end1 + end2 + end3
print end4 + end5 + end6

print "\n"
height = raw_input("How tall are you? ")
print height
print "So you are %r" % height # if i pass %d - will throw error because raw_input returns string and %d - expect digit
# so we are passing %r raw representation of input and it works