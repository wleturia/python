"""
Assignment: 
a
b
c

for apple
for banana 
for cherry


a for apple
b for banana
c for cherry

"""
with open("atoc.txt",'w') as f1, open("fruits.txt",'w') as f2:
	f1.write("a\n")
	f1.write("b\n")
	f1.write("c\n")
	f2.write("for apple\n")
	f2.write("for banana\n")
	f2.write("for cherry\n")


from itertools import izip

with open("res.txt",'w') as res, open("atoc.txt") as f1,open("fruits.txt") as f2:
	for line1,line2 in zip(f1,f2):
		res.write("{} {}\n".format(line1.rstrip(),line2.rstrip()))

"""
for i in izip([1,2,3],['a','b','c']):
	print i
"""