help(str)

order = '1,2013-07-25 00:00:00.0,11598,CLOSED'

orderStatus = order.split

help(str.split)

l = [1,2,3,4]

type(l)

order.split(",")



l[0]

l[3]

order.split(",")[3]

order.split(",")[0]

type(order.split(",")[3])


10 > 2

'10' > '2'

int(order.split(",")[0])

if (order.split(",")[0].isdigit()):
	i = int(order.split(",")[0])

i

type(i)

#____________________________________________________

len(order)

order

help(order.count)

order.count("00")

order


order.count("00",2,18)

help(order.index())

order.index("00")

order

order.index("000")

order.find("000")

orderStatus = order.split(",")[3]

orderStatus #CLOSED

orderStatus.lower()

orderStatus.upper()

orderStatus.capitalize()

s = "HellO wORLd"

s.capitalize()

s = "Hello              "
s = "            Hello              "
s.lstrip()
s.rstrip()


#2013,7,25 -> 2013-07-25

m = 7

help(str.ljust)


str(m).ljust(2, "0") #70
str(m).rjust(2, "0") #07

year = 2013
month= 7
date = 25

"-".join([str(year), str(month),rjust(2,"0"),str(date).rust(2,"0")]) #2013-07-25


order

orders = '1,2013-07-25 00:00:00.0,11598,CLOSED\n2, 2013-07-25 00:00:00.0,100,COMPLETE'

orders

orderList = orders.split("\n")

orderList

orderList = orders.splitlines()

orderList

orderStatus

orderStatus.isupper()

order

order.isalnum()

order.isprintable() #True