f=None
try:
	f=open("sampl.txt","r")
except FileNotFoundError:
	print("File not found")
else:
	print(f.read())
finally:
	print("This is from finally clause")
	if f:
		f.close()