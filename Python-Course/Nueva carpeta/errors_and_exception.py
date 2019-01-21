#4 + x * 5

#Error x is not defined



#2 + 'x '

#Unsupported operant types

 
while True:
	try:
		x = int(input("Please enter a number"))
		break
	except ValueError:
		print("Oops! It is not a valid number. Try again...")
	except (RuntimeError, TypeError, NameError):
		pass
	finally:
		print("You have typed " + str(x))
