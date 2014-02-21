#finding chip
#this program is a simple game in which you traverse through an apartment looking for the beloved family dog. however, dog can only be lured with proper inventory

#this creates an empty inventory for our hero 
cur_inv = []

#here we define the goal items (to be used in Living Room & Bathroom)
treat = "Dog Treat"
toy = "Chew Toy"
#deprecated these values. replaced with function below due to bug discovered through UAT. User was unable to complete game as they added multiple 'toys' to inv. then goal was not met. function now just checks if they have BOTH items in inv.
goal = [treat, toy]
goal2 = [toy, treat]

def goal(list):
	if treat in list and toy in list:
		return True
	else:
		return False
		
#response = raw_input("Append Values? \nY/N? \n> ")

#if response == "Y":
#	cur_inv.append(treat)
#	cur_inv.append(toy)

#print cur_inv == goal 

print ">>You walk up to the door in your typical daze. It dawns on you the 3202 outside the door means you're home. 'Wow' you think. '6p already?' Today flew by, but at least you're home"

#this function allows us to ask user to open front door. if they do not open, function will continue to run (IE they will have to open the door)
def start():
	door = raw_input(">>Open apartment door? \n>>Y/N?\n>").lower()
	if door == "y":
		print ">>Welcome Home! Unfortunately, you're shocked at what you see! There is garbage EVERYWHERE"
		print ">>Literally, everywhere. And your dog Chip is no where to be seen. At least we have a suspect..."
		clean_garbage()
	else:
		print ">>You have to open it"
		start()

		
def clean_garbage():
	print ">>Well it looks like you can either clean all this up, or attempt to jump over it."
	print ">>What do you want to do?"
	answer = raw_input(">>Clean or Jump?\n>").lower()
	if answer == "clean":
		print ">>Good choice. It takes you about 45 minutes, but you finally clean up the garbage blocking the rest of the aparment"
		choose_next()
	elif answer == "jump":
		print ">>Yikes....valiant effort, but you barely clear the water bottles at the entry way. You slip on some rotting lasagna and die. Bummer!"
	else:
		print ">>You can %s later, but right now you either need to clean or jump. No other way around this mess." % answer
		clean_garbage()

def choose_next():
	print ">>Ok, where should we go next?"
	next = raw_input(">>living room? bathroom? bedroom?\n>").lower()
	if next == "living room":
		living_room()
	elif next == "bathroom":
		bathroom()
	elif next == "bedroom":
		bedroom()
	else:
		print ">>As nice as it would be to have a %s, that doesn't exist. Try again" % next
		choose_next()

def living_room():
	print ">>You enter the living room"
	print ">>Nothing here but pillows everywhere."
	print ">>Wait! You spot something on the floor! %s is added to your inventory!" % treat
	cur_inv.append(treat)
	choose_next()

def bathroom():
	print ">>You enter the bathroom"
	print ">>No suprise here. Lots of mess, but no Chip."
	print ">>What's that green thing in the tub........"
	print ">>Luckily it's a chew toy (you assumed the worse....). %s is added to your inventory!" % toy
	cur_inv.append(toy)
	choose_next()

def bedroom():
	print ">>You enter the bedroom"
	print ">>You hear a loud BARK! Chip must finally be close, but where?"
	check_places()

def check_places():
	check = raw_input(">>Where should we check? \n>>under bed? closet? balcony? \n>").lower()
	if check == "closet":
		print ">>Nothing here....try again."
		check_places()
	elif check == "under bed":
		print ">>You find him! But he won't come out from under the bed...."
		if goal(cur_inv) == True:
			end()
		else:
			print ">>You should search the house for things that might help you lure him out."
			print ">>Let's go back to the kitchen to search!"
			choose_next()
	elif check == "balcony":
		print ">>Nothing out here. Smells like pee and poop though. Try again"
		check_places()
	else:
		print ">>That doesn't exist....what is %s anyways? Try again" % check
		check_places()

def end():
	print ">>Nice! You lured Chip from out under the bed with the %s and %s" % (treat, toy)
	print ">>Now to talk to him about the mess....."
	print ">>Thanks for playing!"


	
start()

