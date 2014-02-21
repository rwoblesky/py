# this program will create a list. size will be specified first, then a while loop will run to collect values

size_of_list = raw_input("How big would you like to make this list? Tell me a number")

size_of_list = int(size_of_list)

print "Ok, so you'd like %d sized list." % size_of_list

list = []

while size_of_list > len(list):
	list.append(raw_input("Value? > "))
	left = size_of_list - len(list)
	print "You have %d inputs left" % left

print list