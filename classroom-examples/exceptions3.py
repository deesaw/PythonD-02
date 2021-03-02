try:
	f=open("sampl.txt","r")
except Exception as err:
	print("File not found")
	print(err)
	print(type(err))
else:
	f.close()