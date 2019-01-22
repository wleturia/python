def printMax(x,y):
	x = int(x)
	y = int(y)

	if(x > y):
		print(x, "is maximun")
	else:
		print(y, "is maximun")


printMax(2,3)



def printMax(x,y):
	"""PRINTS THE MAXIMUN OF TWO NUMBERS
	BOTH THE NUMBERS SHOULD BE INTEGERS"""
	if(x > y):
		print(x, "is maximun")
	else:
		print(y, "is maximun")

printMax(2,3)

printMax.__doc__()



def min_max(numbers):
	smallest = largest = numbers[0]
	for item in numbers:
		if item > largest :
			largest = item
		elif item < smallest:
			smallest = item
	return smallest,largest

min_max([1,2,5,3,7,8,4])

smallest, largest = min_max([1,2,5,3,7,8,4])

smallest

largest 