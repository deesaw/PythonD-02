#tuples are read only list
tu = (5,6,7,8,9,5)
print(type(tu))
print(len(tu))
print(tu.count(5))

#operators on tuple
tu = (5,6,7,8)
tu1= 8,9,10,11
print(tu+tu1)                #Concatenates two tuples
print(tu*2)
print(7 in tu)
print(8 not in tu)

#Indexing 
print(tu[3])
print(tu[1:5])
print(tu[:])
print(tu.index(7))            #returns the index positon of 7

tu=(10,20,5,40,30)
#Cannot modify a tuple, returns Type Error
#tu[3] = 100
#cannot remove an element from tuple, returns Attribute Error
#tu.remove(20)              
