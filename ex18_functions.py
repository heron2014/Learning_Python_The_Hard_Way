"""
Functions do 3 things:
\t * They name pieces of code the way variables name strings and numbers
\t * They take arguments the way your scripts take argv
\t * Using 1 and 2 they let you make your own "mini-script" or "tiny commands"
"""

#*args = all arguments


def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r " % (arg1, arg2)


def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


def print_one(arg1):
    print "arg1: %r" % arg1


def print_none():
    print "I got Nothing"


print_two('Hi', 'Babe')
print_two_again('Hola', 'Babe')
print_one('Helloooo')
print_none()

