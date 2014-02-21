print " You enter a dark room with two doors. Do you go thru door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print " There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake"
	print "2. Scream @ the bear"
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good Job!"
	elif bear == "2":
		print " The bear eats your legs off. Good Job!"
	else:
		print "Probably a good choice not going with 1 or 2. Bear runs away!"

elif door == "2":
	print "You stare into the endless abyss of Cthlhu's retina"
	print "1. Blueberries"
	print "2. Yellow Jacket Clothespins"
	print "3. Understanding revolvers yelling melodies"
	
	insanity = raw_input("> ")
	
	if insanity == "1" or instanity == "2":
		print "Your body survices powered by a mind of Jello. Good Job!"
	else:
		print "The insanity rots your eyes into a pool of much. Good Job!"
else:
	print" You stumble around looking for door #%s and fall on a knife and die. nice!" % door