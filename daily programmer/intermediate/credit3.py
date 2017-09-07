# Python 3
#Converts an user inputed amount to words, handles upto 100 trillion

def atow(x):

	x *= 100
	change = int (x % 100)
	x = int (x / 100)

	if change == 0:
		cent = "zero"
	else:
		cent = switch(change)

	if x == 0:
		final = "zero dollars and " + cent + " cents."
	else:
		final = switch(x) + " dollars and " + cent + " cents."

	return final

# convert number to string
def switch(x):
	switcher ={
				0 : "", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10: "ten",
				11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
				20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninty",
	}

	# keep track of the number and return appropriately
	if x > 20 and x % 10 != 0 and x <= 99:
		return switcher.get(x - (x % 10)) + " " + switcher.get(x % 10)
	if x >= 100 and x < 1000:
		return switcher.get(int(x / 100)) + " hundred " + switch(x % 100)
	if x >= 1000 and x < 1000000:
		return switch(int(x / 1000)) + " thousand, " + switch(x % 1000)
	if x >= 1000000 and x < 1000000000:
		return switch(int(x / 1000000)) + " million, " + switch(x % 1000000)
	if x >= 1000000000 and x < 1000000000000:
		return switch(int(x / 1000000000)) + " billion, " + switch(x % 1000000000)
	if x >= 1000000000000 and x < 1000000000000000:
		return switch(int(x / 1000000000000)) + " trillion, " + switch(x % 1000000000000)
	return switcher.get(x, "")