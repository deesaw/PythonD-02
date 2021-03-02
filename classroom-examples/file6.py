#Write a function that returns the number of
#lines,words and characters in a file

def get_file_details(filename):
	f=open(filename,"r")
	contents = f.read()
	f.close()
	lcount = len(contents.split("\n"))
	wcount = len(contents.split())
	ccount = len(contents)
	return lcount, wcount, ccount

linecount,wordcount,charcount = get_file_details("sample.txt")
print(linecount,wordcount,charcount)