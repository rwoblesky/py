# this one is like your scripts with argv
def define ():
	arg1 = raw_input("One")
	arg2 = raw_input("Two")
	return arg1, arg2
	
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that * args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one arguement
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguements
def print_none():
	print "i got nothin'."

define()
print_two_again(arg1, arg2)
print_none()
