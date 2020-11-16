from abc import ABC, abstractmethod
from typing import List

class Course():
	def __init__(self, course_name):
		self.__name = course_name
		
	def get_name(self):
		return self.__name

class Agent():
	
	@abstractmethod
	def get_age(self):
		pass
	
	@abstractmethod
	def set_age(self, age):
		pass

class Person(Agent):
	
	def __init__(self, age : int = 0):
		self._age = age
		
	def get_age(self) -> int :
		return self._age
		
	def set_age(self, age : int) -> None:
		self._age = age
		
class Student(Person):
	
	def __init__(self, exams_todo : List[str], exams_passed : List[str] = []):
		self.__exams_todo : exams_todo
		self.__exams_passed : exams_passed
		
	def give_exam(self, course : Course, grade : int) -> None:
		if course in self.__exams_todo:
			self.__exams_passed.append(course)

class Professor(Person):
	pass

class Course():
	
	def __init__(self, id : int, name : str, degree : str):
		self.__id = id
		self.__name = name
		self.__degree = degree
		
	def get_id(self) -> int:
		return self.__id
		
	def get_name(self) -> str:
		return self.__name
		
	def get_degree(self) -> str:
		return self.__degree	
	
class Artefact(ABC):
	
	@abstractmethod
	def say_hi(self):
		pass
    
class Robot(Artefact):    
    def __init__(self, name):
        self.name = name
    
class Physician(Artefact):
	def __init__(self, specialisation):
		self.specialisation = specialisation
	 
class PhysicianRobot(Robot, Physician):
	
	def __init__(self, name, spec):
		Robot.__init__(self, name)
		Physician.__init__(self, spec)
	
	def say_hi(self):
		print("Hi, my name is " + self.name + " and my specialisation is " + self.specialisation)
		
if __name__ == '__main__':
	Jim = Person()
	Jim.set_age(10)
	print("Person age", Jim.get_age())

	robot = PhysicianRobot("Marvin", "Cardiovascular surgery")
	robot.say_hi()

	robot = "I am a robot"
	print(robot)

	robot = 24
	print(str(24))

	robot = ['I', 'am', 'a']
	robot.append('robot')
	for i in robot:
		print(i)
