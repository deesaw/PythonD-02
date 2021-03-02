#Create a list of 1000 random numbers
import random

r =[]
for i in range(1000):
	r.append(random.randint(1,100))

#Print how many times each number is present in the list.
#Find unique numbers
#Find their counts
for i in set(r):
	print("Number {} repeated {} times".format(i,r.count(i)))

#Print all numbers which repeated more than 5 times.
print("#" * 50)
for i in set(r):
	if r.count(i) > 5:
		print("Number {} repeated {} times".format(i,r.count(i)))
#Dictionary approach
d={}
for i in set(r):
	d[i] = r.count(i)


print(d)
