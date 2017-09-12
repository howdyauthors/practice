# Python 3

def check(x, y):
	if x < 0 and y < 0:
		return 0
	elif x < 0 or y < 0:
		if x < 0:
			return x
		elif y < 0:
			return y
	else:
		return 2

def mult(x, y):
	if x == 0 or y == 0:
		return 0
	result = 0
	checksign = check(x, y)
	for i in range (abs(y)):
		result += abs(x)
	if checksign == 0 or checksign == 2:
		return result
	elif checksign == x or checksign ==y:
		return sub(result, result + result)


def sub(x, y):
	result = 0
	if y < 0:
		temp = 1
	else:
		temp = -1
	junk = 0
	for i in range (abs(y)):
		x += temp
	return x


def div(x, y):
	if y == 0:
		print("Not-defined")
		exit(1)
	junk, result = abs(x), 0
	checksign = check(x, y)
	while junk != 0:
		if junk < y:
			return None
		result += 1
		junk = sub(junk, abs(y))
	if checksign == 0 or checksign == 2:
		return result
	elif checksign == x or checksign ==y:
		return sub(result, result + result)
	return 0


def exp(x, y):
	if x == 0:
		return 0
	if y == 0:
		return 1
	if y < 0:
		return None
	result = x
	checksign = check(x, y)
	for i in range (1, abs(y)):
		result = mult(result, x)
	if x < 0 and mult(y, 2) == None:
		return sub(result, result + result)
	else:
		return result


def main():
	x = int(input("Enter the first operand: "))
	y = int(input("Enter the second operand: "))
	operation = input("Enter the operation '+', '-', '*', '/' or '^': ")
	if operation == '+':
		print("{}".format(x + y))
	elif operation == '-':
		print("{}".format(sub(x, y)))
	elif operation == '*' or operation == 'x':
		print("{}".format(mult(x, y)))
	elif operation == '/':
		final = div(x, y)
		if final == None:
			print("Not an integer")
		else:
			print("{}".format(final))
	elif operation == '^':
		final = exp(x, y)
		if final == None:
			print("Not an integer")
		else:
			print("{}".format(final))

	return 0


if __name__ == "__main__":
	main()
