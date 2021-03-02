fruits=['apple','pear','grapes','orange']

for fruit in fruits:
	print(fruit)

for fruit in fruits:
	print(fruit.upper())

for index,fruit in enumerate(fruits):
	print(index,fruit)

marks={'Maths':97,'Science':98,'History':78}
for index,subject in enumerate(marks):
	print(index,subject,marks[subject])

for key in marks:
	print(key)

for key in marks:
	print(key,marks[key])

for key in marks:
	print ("I scored {} marks in {}".format(marks[key],key))