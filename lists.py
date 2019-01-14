a = ['python',1223,'python1222']
print(a)

#Access update delete list

a =['python',12.33]
print(a[0]) #python

a[1] = 'hello' #updates second value

del a[1]
print(a) #['python']


#Max Method

a=[1,2,3,4,123,123,333]
print(max(a)) #333

#Min Method

a=[1,2,3,4,123,123,333]
print(min(a)) #1

#Count Method

a=[1,2,3,4,123,123,333]
print(a.count(123)) #2

#Index Method

a=[1,2,3,4,123,123,333]
print(a.index(123)) #if repeats show the last one

#Append Method
a=[1,2,3,4,123,123,333]
a.append('hello')
print(a)

#Insert Method - need index

a=[1,2,3,4,123,123,333]
a.insert(2,'hello')
print(a)

#Reverse Method

a=[1,2,3,4,123,123,333]
a.reverse()
print(a)

#Sort Method
a=[1,2,3,4,123,123,333]
a.sort() #increase
a.reverse() #decrease
print(a)
