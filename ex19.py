def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "you have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party"
	print "Ger a blanket. \n"

print "We can just give the function numbers directly"
cheese_and_crackers(20, 30)

print "OR, we can use the variables from our script:"
amount_of_cheese = int(raw_input())
amount_of_crackers = int(raw_input())

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
