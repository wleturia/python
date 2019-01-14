x=int(input('enter a number '))
print(x)

#With exception

while True:
	try: 
		x = int(input("enter a number "))
		break
	except:
		print("Please write something correctly")
	finally:
		print("over")