#Write a function to check if a string is a palindrome.
#(what is a palindrome? A word that reads the same in both directions ex: "aha","malayalam")
def ispalindrome(word):
	return word == word[::-1]


print(ispalindrome("aha"))
print(ispalindrome("deloitte"))

#Write a function to print the number of lines in a file.
def linecount(filename):
	f=open(filename,'r')
	lines=f.readlines()
	f.close()
	return len(lines)

print(linecount("exercises.txt"))
print(linecount("1.py"))

#Write a function to print the factorial of a number.
def factorial(n):
	f=1
	for x in range(2,n+1):
		f=f*x
	return f


print(factorial(2) == 2)
print(factorial(3) == 6)
print(factorial(4) == 24)
print(factorial(10))
print(factorial(1))
print(factorial(0))


#Write a function that returns a list of all the indexes of a char in a string.
def get_indices(word,char):
	listofindices = []
	for index,mychar in enumerate(word):
		if mychar == char:
			listofindices.append(index)
	return listofindices


print(get_indices("banana","a") == [1,3,5])
print(get_indices("deloitte","t") == [5,6])
print(get_indices("elephant","e"))
print(get_indices([3,4,5,6,4,4,5],4))

