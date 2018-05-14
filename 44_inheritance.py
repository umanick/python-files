class Parent1(object):

	def implicit(self):
		print "PARENT implicit()"

class Child1(Parent1):
	pass

dad1 = Parent1()
son1 = Child1()

dad1.implicit()
son1.implicit()

class Parent2(object):

	def override(self):
		print "PARENT2 override()"

class Child2(Parent2):

	def override(self):
		print "CHILD2 override()"

dad2 = Parent2()
son2 = Child2()

dad2.override()
son2.override()

class Parent3(object):

	def altered(self):
		print "PARENT3 altered()"

class Child3(Parent3):

	def altered(self):
		print "CHILD3, BEFORE PARENT3 altered()"
		super(Child3, self).altered()
		print "CHILD3, AFTER PARENT3 altered()"

dad3 = Parent3()
son3 = Child3()

dad3.altered()
son3.altered()
