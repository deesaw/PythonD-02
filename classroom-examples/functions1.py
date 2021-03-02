
def hello():
	print("Hello how are you")

hello()


def add(a,b):
	return a + b

print(add(5,6))

c = add(12,34)

print(c)

#default arguments
def product(a,b=10):
	return a * b

print(product(5,6))
print(product(5))

c = product(12,34)

print(c)


# keyword arguments

def wish(name,age):
	print("Hello {} you are {} years old".format(name, age))

wish("India",73)
wish(73, "India")

wish(age=73, name="India")





