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
class Student(object):
	"""Defines commonalities among students"""


	def __init__(self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address


class Question(object):
	"""A dictionary to store questions and their correct answers"""


	def __init__(self, question, correct_answer):
		self.question = question
		self.correct_answer = correct_answer
		exam = {}
		exam[question] = correct_answer ##setting up a new dictionary to 
		# hold all question/answer key value pairs



	def ask_and_evaluate(self, question): 
		"""Part 3.2: Prompt user to answer question and then evaluate whether user_answer
		is correct."""
		

		user_answer = raw_input(question)
		if user_answer == correct_answer:
			return True

		

class Exam(Question):
	"""docstring for Exam"""
	
	def __init__(self, exam_name, question): 
		self.exam_name = exam_name
		self.questions = []

	
	def exam_question(self, question, correct_answer):
		"""not sure how to answer Part 3.1: in order for the method to take 
		question, correct_answer as parameters, I'm thinking class Exam must be 
		inheriting from class Question. Otherwise there is no definition for 'question' 
		and 'correct answer' within this class. """

		exam_question = {} #creating an empty dictionary 
		#for list of exam_questions
		for question, correct_answer in exam.items(): #iterate over each item in exam
		#dictionary
			exam_question.add(question, correct_answer) #add those key value pairs to new dictionary of 
			#of exame questions
				return exam_question #return the full list

	def exam_administer(self, exam_question):
		"""Part 3.4: adminster the exam"""


		score = 0
		for question in exam_question:
			if ask_and_evaluate(question) is:
				score += 1
		#in a dictionary, not sure how to gauge when the last key/value
		#pair has been iterated. (Part 3.4)
			



		


		

		
		
		
		
