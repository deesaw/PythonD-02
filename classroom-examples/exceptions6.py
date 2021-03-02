def factorial(n):
	if n < 0:
		raise ValueError("n must be greater than 0")
	f=1
	for x in range(2,n+1):
		f*=x
	return f


print(factorial(5))
print(factorial(10))
print(factorial(-1))