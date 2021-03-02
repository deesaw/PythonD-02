friends = ["hari","sita","lalitha","vishal"]
print(list(map(len,friends)))
print(list(map(type,friends)))

def reverse(word):
	return word[::-1]

print(list(map(reverse,friends)))
print(list(map(lambda x:x[:3] ,friends)))

numbers = [45,78,34,12,98,45]

print(list(map(lambda x:x**2 ,numbers)))
print(list(map(lambda x:x**3 ,numbers)))


#print factorials of numbers
#using the map and factorial function in the math module

from math import factorial
print(list(map(factorial ,numbers)))













