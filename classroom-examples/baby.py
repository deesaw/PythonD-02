class Baby:
	def __init__(self,name=None):
		self.name = name
	def laugh(self):
		print("ha..ha..ha")
	def cry(self):
		print("I am crying")
	def hi(self):
		print("Hello I am {}".format(self.name))