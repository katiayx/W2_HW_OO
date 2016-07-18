"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   abstraction = class have well-defined logic, and users of class do not need to know all the ins and outs of how the class works. 
   polymorphism = flexibility that allows certain attributes to apply to multiple sub-classes
   encapsulation = allows components to be bundled together

2. What is a class?
	A way to organize data and methods to simplify code structure in a logical manner

3. What is an instance attribute?
	A trait that is particular to an instance of a class; the object of the class. Differs from class attribute
	because class as a whole does not have this attribute

4. What is a method?
	A function that's defined on a class

5. What is an instance in object orientation?
	an object that belongs in a class: because it shares enough class attributes to qualify itself as a member of this class


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    class attributes are traits that are applicable to most of the instances of the class - All animals eat food
    Instance attribute are traits that are specific to that particular instance - Camel of the Animal class all have humps


"""


# Parts 2 through 5:
# Create your classes and class methods

class Plants(object):
	"""defines what make plants plant"""
	

	eat = sunlight

	def __init__(self, name, color)
		self.name = name
		self.color = color

	def what_are_you(self, species):
		if self.species = root:
			print "{}! You are a root plant of {} species".format(self.name, self.species)
		else:
			print "{}! You are a non-root plant of {} species".format(self.name, self.species)

class Veggies(Plants):
	"""veggies are part of Plants class"""
	
	color = green

class Flowers(Plants):

	def what_are_you(self):
		super(Flowers, self).what_are_you(species) 
		
		
