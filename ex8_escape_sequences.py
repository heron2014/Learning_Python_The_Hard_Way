import datetime
tobby_cat = "\t I'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tobby_cat
print persian_cat
print backslash_cat
print fat_cat

# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" % i,

y ='#' * 5
z = "escape sequences"
x = "Hello I will be using few  %s \nfor you to understand the concept.\nNow \t%r" % (z, y)
print x

b = datetime.datetime.now()
b.strftime("%A %d. %B %Y")
s = "\\today and tomorrow is gonna be \"Amazing\"---today is \n %r " % b

d = "\\today and tomorrow is gonna be \"Amazing\"---today is \n %s " % b.strftime("%A %B %Y")
print s

print d
"""
this is treated like a comment because its not assign to any variable
and we do not print it
"""