#file = open('python.txt', 'w+') #Creates a new file

#Reading from a File

f = open("python.txt",'r')
f.read(5)
f.read()
f.tell()
print (f.read())

for line in f:
    print (line)

f.seek(0)
f.readline()

f.seek(0)
f.readlines()


#Writing Files

file = open('python.txt','w')
#str = "Hello world! this is a new message"
str = input("Mensaje: ")

file.write(str)
file.close()


#Appending Files

file = open('python.txt','a')
str = input("enter some append data: ")
file.write(str)
file.close()

#Download File from internet

import urllib.request

urllib.request.urlretrieve("https://http2.mlstatic.com/carro-con-luz-musica-y-movimiento-carrito-juguete-nino-cars-D_NQ_NP_758299-MLV25794926388_072017-F.jpg","hackiao.jpg")