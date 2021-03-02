class Dog:
	def __init__(self,color,breed):
		self.color = color
		self.breed = breed
	def speak(self):
		print("Bhou..bhou")
	def guard(self):
		print("I am guarding your home")

tommy = Dog("brown","labrador")
print(type(tommy))
print(isinstance(tommy,Dog))

tommy.speak()
tommy.guard()
print(tommy.color)
print(tommy.breed)

