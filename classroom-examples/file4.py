#based on marks.csv
#print the student name and total marks

f=open("marks.csv","r")
for line in f:
	name,sub1,sub2,sub3 = line.split(",")
	total = int(sub1) + int(sub2) + int(sub3)
	print("{} scored {} marks".format(name,total))
f.close()
