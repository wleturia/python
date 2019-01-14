#Functions

def python():
	print("Hello")
	return

python()


#Arguments

def hello(name):
	print("hello " + name + "!")
	return

#hello(name= "Walter")
hello("Walter")


#if is not set use a default value
def hello2(x,y=500):
	print(x,y)
	return 

hello2(24)
hello2(24,23)

#Store multiple values in value l *

def hello3(x,*l):
	print(x)
	for b in l:
		print b
	return

hello3(12)
hello3(12,34,45,65)


#Past by value 

x = 13
def hello4(x):
	x = 45
	print(x)
	return 

hello4(x)
print(x)

#Past by Reference
a=[1,2,3,4]

def hello5(x):
	x[0] = 12
	print(x)
	return 

hello5(a)
print a