s= "Hello"

print(s*4)

def say(s, times = 1):
	print(s * times)

say("Hello")

say("Hello",4)

help(str.split)

def func(a,b = 5, c= 10):
	print('a is ', a, 'b is ', b, 'and c is ', c)


func(3,7)

func(25,c=24)


func(c = 50, a= 100)


def total(initial = 5, *numbers):
	count = initial
	for num in numbers:
		count + = num
	return count

total(10,1,2,3,4)


def total(initial = 5, *numbers, **keywords):
	count = initial
	for num in numbers:
		count + = num

	for key in keywords:
		count += keywords[key]
	return count

total(10,1,2,3,vegetables = 50, fruits = 100)