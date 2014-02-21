def split_word(word):
	place = 0
	split = []
	while place < len(word):
		split.append(word[place])
		place += 1
	return split

def sort_split(a):
	a.sort()
	return a

split = split_word(raw_input("What would you like to split?"))
print split


print "Would you like to sort?"
response = raw_input("Y or N")

if response == "Y":
	print sort_split(split)
else:
	print "alright then"

for a in split:
	print a