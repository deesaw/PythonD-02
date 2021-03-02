class Car:
	def __init__(self,seatcount,regno=None):
		self.seatcount = seatcount
		self.regno = regno
	def __str__(self):
		return f"I am a {self.seatcount} seater car."
	def __len__(self):
		return self.seatcount
	def __bool__(self):
		if self.regno:
			return True
		else:
			return False
	def __add__(self,other):
		return self.seatcount + other.seatcount
	def __iter__(self):
		pass
	def __next__(self):
		pass

swift  = Car(5)
innova = Car(7,"AP26 AA909")

print(swift)
print(innova)

print(len(swift))
print(len(innova))

print(bool(swift))
print(bool(innova))

print(swift + innova)


for passenger in swift:
	print(passenger)