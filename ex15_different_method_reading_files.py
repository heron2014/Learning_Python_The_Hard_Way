from sys import argv

script = argv

print 'This is your: \n', script

print 'Open a text file which name is : ex15_sample.txt\n'

my_file = raw_input('Type the filename: ')

my_file_txt = open(my_file)
print '\n'
print my_file_txt.read()

my_file_txt.close()