people = raw_input('Number of people?')
cats = raw_input('Number of cats?')
dogs = raw_input('Number of dogs??')

if people < int(cats):
	print "Too many cats!"

if people > int(cats):
	print "not enough cats!"

if people < int(dogs):
	print "The world if drooled on!"
	
if people > int(dogs):
	print "The world is dry!"
	
dogs = int(dogs) + 5

if people >= int(dogs):
	print "peple are greater than or equal to dogs"

if people <= int(dogs):
	print "People are less than or equal to dogs"

if people == int(dogs):
	print "People are dogs"