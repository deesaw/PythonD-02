from functools import reduce

numbers = [45,78,34,12,98,45]

print(reduce(lambda a,b:a+b,numbers))
print(reduce(lambda a,b:a*b,numbers))