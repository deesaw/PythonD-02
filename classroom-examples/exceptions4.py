def divide(a,b):
	try:
		output = a/b
	except ZeroDivisionError:
		print("Check your denominator")
	except TypeError:
		print("This works with numbers only")
	else:
		print(output)

divide(10,3)
divide(10,0)
divide("a","b")