import ex42
## rover is- a Dog
rover = ex42.Dog("Rover")

## Satan is a Cat
satan = ex42.Cat("Satan")

## Mary is a person with no cat or salary
mary = ex42.Person("Mary")
mary.pet = satan

## Frank is a person with a Dog as and has a salary
frank = ex42.Employee("Frank", 120000)
frank.pet = rover
mary.marry(frank)

mary.printme()
frank.printme()
## ??
flipper = ex42.Fish()
flipper.printme()
## ??
crouse = ex42.Salmon()
crouse.printme()
## ??
harry = ex42.Halibut()
harry.printme()

print issubclass(ex42.Employee, ex42.Person)
