a = {2007: 'hello'}
#key and value

#use the key to access the value
a[2007]


#METHODS

#Len Method
a = {2007: 'hello', 2008:'world'}

print(len(a))

#Clear Method

a.clear()
print(a)

#Copy Method

b = a.copy()
print(b)

#Get Method

print(a.get(2008)) #retrieves world
print(a.get('world')) #retrieves 2008


#Items Method

print(a.items())

#Print Key Methods

print(a.keys())

#Update Method
a = {2007: 'hello', 2008:'world'}
b = {2008: 'hello', 2009:'world'}

a.update(b)

print(a)

#Values Method

print(a.values())


#Access Update Delete Dictionary
a = {2007: 'hello', 2008:'world'}

print(a[2007]) #Access

a[2007] = 'Python' #Update

a[2009] = 'Hello World' #Add

del a[2007]

print(a)