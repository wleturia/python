class Father():
	def lastname(self):
		print("my sirname")

class Mother():		
	def lastname2(self):
		print("my sirname 2")


class Son(Father, Mother):
	def firstname(self):
		print("my firstname")


s1 = Son()
s1.firstname()
s1.lastname()
s1.lastname2()
