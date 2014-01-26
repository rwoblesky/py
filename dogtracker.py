#this is a program that will take parameters and write to a .csv file
print "Hi! Welcome to Dog Tracker 2000. This program will create a txt file in the target directory and allow you to add a list of dogs you know. Future enhnacements will allow editing of files, however for now only creating new txt files is supported"
print "First, let's name this new file"
prompt = "> "

filename = (raw_input(prompt))
print "Nice! I like the name %s" % filename 
filename = filename + ".csv"
print "Just so you know, to make it open via a text editor, we've created the csv for you %s" % filename 

target = open(filename, 'w')

#this line initiates the text file with proper headers (for excel)


target.write("Dog Name, Dog Breed, Dog Weight, Dog Age")
target.write("\n")

def get_values(list):
	i = 0
	while i < 4:
		value = raw_input(prompt)
		list.append(value)
		i = i + 1

def write_to_file(list):
	for a in list:
		target.write(a)
		target.write(",")
		
def get_multiple_values():
	question = "Add Values?"
	print question
	response = raw_input("Y/N")
	while response == "Y":
		values = []
		get_values(values)
		write_to_file(values)
		target.write("\n")
		print question
		response = raw_input("Y/N")


get_multiple_values()

print "Nice! Check the file for the output"	
		