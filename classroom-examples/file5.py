#based on marks.csv
#print the student name and total marks
import csv
f=open("marks.csv","r")
for row in csv.reader(f):
	name,sub1,sub2,sub3 = row
	marks =[]
	for subject in row[1:]:
		marks.append(int(subject))
	print("{} scored {} marks".format(name,sum(marks)))
f.close()