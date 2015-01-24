from sys import argv

script, user_name = argv
prompt = '> '

user_name = raw_input("What's your name? ")
print "Hi %s! I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = str(raw_input(prompt))
no_var = 'no'

if likes == no_var:
    print "Screw you, then!"
elif likes == 'yes':
    print "Ohh wow, That's awkward because I don't like you "
else:
    print "I can live with that"

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said: \'%r\' about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. Not as I care!
""" % (likes, lives, computer)
