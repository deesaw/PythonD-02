friends = ["hari","sita","lalitha","vishal"]

print(list(filter(lambda x:len(x)==4,friends)))
print(list(filter(lambda x:len(x)>4,friends)))


numbers = [45,78,34,12,98,45]

#pick only odd numbers using filter

print(list(filter(lambda x:x%2!=0,numbers)))
