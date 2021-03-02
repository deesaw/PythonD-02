"""
Write a program
that will search for 
a pattern in a file
and print all the matching
lines along with line numbers
"""
filename = "1.py"
pattern = "print"


def searchfile(filename,pattern):
	f=open(filename,"r")
	for lineno,line in enumerate(f):
		if pattern in line:
			print(lineno + 1,line,end="")
	f.close()
	
searchfile(filename,pattern)