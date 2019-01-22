#def sumOfIntegers(lb,ub): 1 to 100 (ub * (ub+1) / 2 - ((lb-1) * (lb/2))

def sumOfIntegers(lb,ub):
	l = lb - 1
	((ub * (ub +1 )) / 2) - ((1*(1+1))/2)


sumOfIntegers(1,10)

sumOfIntegers(5,10)

range(1,10)

range(1,10+1)

def sum (lb,ub):
	total = 0
	for i in range(lb, ub + 1):
		total += i
	return total

sum(1,10)

sum(5,10)

def sum(lb,ub,f):
	total = 0
	for i in range(lb,ub+1):
		print(f(i))
		total += f(i)
	return total

sum(5,10,lambda i: i)


sum(5,10,lambda i: i * i)

sum(5,10,lambda i: i if(i%2 == 0) else 0)


def getEven(n):
	return n if(n%2 == 0) else 0

sum(5,10,lambda i: getEven(i))