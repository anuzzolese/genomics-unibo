def upper_case(method):
	def up(instance):
		f = method(instance)
		return f.upper()
	
	return up
	
class Person:
	
	def __init__(self, given_name, family_name, age):
		self.__gn = given_name
		self.__fn = family_name
		self.__age = age
		
	@upper_case
	def __get_fn(self):
		return self.__fn
		
	def get_name(self):
		return self.__gn + " " + self.__get_fn()
		
	@property
	def tax_code(self):
		return self.__gn + self.__fn + str(self.__age+2)
	
class Robot():
	def __init__(self, name, specialty):
		self.name = name
		self.__specialty = specialty
	
	def get_name(self):
		return self.name
		
	def set_name(self):
		self.name = name
		
	def get_specialty(self):
		return self.__specialty
		
	def set_specialty(self, new_spec):
		self.__specialty = new_spec		
		

	@property
	def spec(self):
		return self.__specialty
		
	@spec.setter
	def spec(self, specialty):
		self.__specialty = specialty
	
	'''
	This means:
	upper_case(Robot.say_hi)		
	'''
	@upper_case
	def say_hi(self):
		return "hi, my name is " + self.name
	

if __name__ == '__main__':
	robot = Robot("Marvin", "Cardiologist")
	print(robot.say_hi())
	
	person = Person("Giorgio", "Stefano", 28)
	print(person.get_name())
	print(robot.spec)
	robot.spec = "Biologist"
	print(robot.spec)
	
	tax_code = person.tax_code
	print("TAX CODE", tax_code)
	#robot.specialty = "Cardiologist"