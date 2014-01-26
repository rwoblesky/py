from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit Ctrl-C"
print "If you want to do that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines (haiku preferable)"


def ask_for_lines(list):
	i = 0
	while i < 3:
		a = raw_input("line?")
		list.append(a)
		i= i + 1

		
		
def write_to_file(a):
	for x in a:
		target.write(x)
		
b = []
ask_for_lines(b)
		
print "I'm going to write these to the file"
print b
write_to_file(b)
#for x in list:
#	target.write(x)

print "And finally, we close it."
target.close()