class Animal():
	def __init__(self, name="animal", sound='noise'):
		self.name = name
		self.sound = sound
	
	def saySomething(self):
		print("I am {0!s} and I {1!s}".format(self.name, self.sound))

	def __format__(self, format):
		if(format == 'name'):
			return self.name
		elif(format == 'sound'):
			return self.sound
		return 'None'

class Dog(Animal):

	def __init__(self, name="dog", sound='bark'):
		self.name = name
		self.sound = sound

animal = Animal("upen","speak")
dog = Dog("Chiwawa","bark")
animal.saySomething()
dog.saySomething()
#print("It is a {:name} and it {:sound}s".format(Dog()))
print("It is a {:name} ".format(Dog()))
print("It is a {:name} ".format(Animal()))