#opens module "argv" = arguement
from sys import argv
#sets arguements for argv
script, filename = argv
# assigns txt to procedure "open" (which literally launches file -> filename in argv
txt = open(filename)
#prints text + filename
print "here's your file %r:" % filename
#calls txt variable and runs .read prodedure (prints text in file) 
print txt.read()
#prints statement for user then assigns file_again to whatever user inputs (raw_input)
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()