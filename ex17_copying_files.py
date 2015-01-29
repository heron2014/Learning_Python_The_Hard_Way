from sys import argv
from os.path import exists

script, from_file, to_file = argv

print 'Copying from %s to %s' % (from_file, to_file)

# in_file = open(from_file)
in_data = open(from_file).read()

print in_data
print "The input file is %d bytes long" % len(in_data)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# out_file = open(to_file, 'w')
out_file = open(to_file, 'w').write(in_data)

print "Done"
#
# out_file.close()
# in_file.close()