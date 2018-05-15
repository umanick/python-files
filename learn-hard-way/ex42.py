#ex42.py
## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## ??
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ??
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## ??
class Person(object):
	def __dir__(self):
		return ['printme', 'marry']
		
	def __init__(self, name):
		## ??
		self.name = name

		## Person has- a pet of some kind
		self.pet = None
		self.spouse = None
		self.salary = None

	def printme(self):
		if self.spouse == None :
			print '%s is single' % self.name,
		else:
			print '%s is married to %s' % (self.name, self.spouse.name),
		if self.pet == None :
			print ', has no pet',
		else:
			print ', has a pet named %s' % self.pet.name,
		if self.salary == None :
			print ' and has no job.'
		else:
			print 'and has a job with salary %s.' % self.salary

	def marry(self, person): 
		person.spouse = self
		self.spouse = person

## ??
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	def printme(self):
		print 'I am a %s' % self.type

	def __init__(self):
		self.type='Fish'

## ??
class Salmon(Fish):
	def __init__(self):
		self.type='Salmon'

## ??
class Halibut(Fish):
	def __init__(self):
		self.type='Halibut'