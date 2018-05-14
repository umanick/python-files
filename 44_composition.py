class Uncle(object):

	def override(self):
		print "UNCLE override()"

	def implicit(self):
		print "UNCLE implicit()"

	def altered(self):
		print "UNCLE altered()"

class Child(object):

	def __init__(self):
		self.uncle = Uncle()

	def implicit(self):
		self.uncle.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.uncle.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()