class Dog:
	def speak(self):
		print("Bhou..bhou")
	def guard(self):
		print("I am guarding your home")

tommy = Dog()
print(type(tommy))
print(isinstance(tommy,Dog))

tommy.speak()
tommy.guard()