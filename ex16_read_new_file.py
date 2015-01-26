from sys import argv

script, filename = argv


f = open(filename)
f_read = f.read()
print f_read

f.close()