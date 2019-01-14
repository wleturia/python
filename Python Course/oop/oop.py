class Student:
	def __init__(self,names,classes): #Constructor
		self.name = "walter" #Class variable
		self.classes = classes
		self.names = names

	def walk(self):
		print("my name is ",self.names)
		print("my name is ",self.name)
		print("my name is ",self.classes)


s1 = Student('xyz', 12)
s1.walk()


