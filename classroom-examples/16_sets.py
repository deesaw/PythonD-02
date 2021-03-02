
"""
Creating an empty set - To make a set without any elements we use the
set()function without any argument
"""
a=set()
print(type(a))

"""
Sets are mutable but as they are unordered,
we cannot change an element using indexing or slicing.
Indexing/slicing are not supported by sets.

"""
#add() is used to add an element to set
a.add(10)
print(a)

#add multiple elements
a.update([4,5,6,(9,0)])
print(a)

#remove and discard are used to remove elements from the set
b={1,2,3,4,5,6,7,1}
b.remove(3)
print(b)



#sets
ss={1,2,3,4,4,5,5,6}
print (ss)

st={(3,4),5,6,(3,4),80.10,"hello","hai"}
print (st)



s1={"grapes","apple","pear","orange",'tomato'}
s2={'tomato','carrot','beetroot'}
print(s1-s2)
print(s1.union(s2))
print(s1.intersection(s2))


s1={"grapes","apple","pear","orange",'tomato','carrot'}
s2={'tomato','carrot'}



print(s1.issuperset(s2))



