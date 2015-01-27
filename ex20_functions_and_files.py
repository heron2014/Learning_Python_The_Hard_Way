from sys import argv

script, input_file = argv

#f = current_file = input_file
def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file)

print "First let's print the whole file: \n"

#this function takes 1 argument which is current_file
print_all(current_file)

print "Lets rewind, kind of like a tape"

#this function takes the same file as a argument
rewind(current_file)

print "Lets print 3 lines: "

#this function takes 2 arguments : first is current line which we define above and second is still the same file
current_line = 1
print_a_line(current_line, current_file)

#this function takes the same arguments but we increment first argument by 1
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#in all function we used 1 file as argument - which is file_input that we pass in argv as current_file

#seek(0) function is dealing in bytes, not lines. The code seek(0) moves the file to the 0 byte(first byte) in the file
# readline() function returns the \n thats in the file at the end of that line. Inside the readline() is a code that
#scans each byte of the file untill it finds a \n character, then stops reading the file and return what it found so far