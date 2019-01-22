var = 10
var1 = 0


if  var:
	print("Value of var is " + str(var))


if  not var1:
	print("Value of var1 is " + str(var1))



val1 = 5

val2 = 50

if val >= 50:
	print("Val is equal or greater than 50")
elif val1>=10:
	print("Val is equal or greater than 10")
else:
	print("Val is lesser than 10")







count = 0

while True:
	print(count)
	count += 1
	if count >= 5:
		break


for x in range(5):
	print(x)


for x in range(1,10):
	if x % 2 == 0:
		print(str(x) +  " is odd")
	else:
		print(str(x) +  " is even")

for x in range(1,10):
	print(str(x) +  " is odd") if(x%2 == 0) else print(str(x) +  " is even")