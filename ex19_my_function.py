def party_supplier(amount_alco, amount_snacks, people):
    print "We gonna have party for %d people" % people

    print "So we need at least %d beers." % (amount_alco * people)
    print "For that amount of people we need %d snacks" % (people * amount_snacks)
    print "\n\n"


party_supplier(57,58,2)


alco = int(raw_input('How many bottles of wine you gonna drink? '))
snacks = int(raw_input('How many snacks you will have? '))
people_p = 112

party_supplier(alco, snacks, people_p)


party_supplier(alco+200, snacks-20, people_p)


guests = (raw_input('Are you taking any guests with you? '))
if guests == 'yes':
    guests = int(raw_input('How many people: ')) + people_p
else:
    guests = 1 + people_p


party_supplier(alco, snacks, guests)

party_supplier(5* 0.33, 34 *2, 100)
