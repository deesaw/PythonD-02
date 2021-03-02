class Car:
	def __init__(self,seatcount,*passengers):
		self.seatcount = seatcount
		self.passengers = passengers

	def __iter__(self):
		self.counter = 0
		return self

	def __next__(self):
		if self.counter < len(self.passengers):
			output = self.passengers[self.counter]
			self.counter += 1
			return output
		else:
			raise StopIteration

		
	
swift  = Car(5,"Suresh","Ravi","Sunny","Richa","Avinash")
innova = Car(7,"Suresh","Ravi","Sunny","Richa","Avinash","Shrey","Avinab")

for passenger in swift:
	print(passenger)


for sno,passenger in enumerate(innova):
	print(sno,passenger)



