#List
numbers = [2,3,4,5,100,4,20,40,50,4]

print(type(numbers))
print(len(numbers))
print(sum(numbers))          #sum of all the elements in the numbersst
print(min(numbers))          
print(max(numbers))


#accessing values from the numbersst
print(numbers[5])
print(numbers[3:7])
print(numbers[6:])

#appending values to the numbersst
a=[50,30,80,90,100,30,140,30]
a.append(70)
print(a)

#inserting values at particular position
a.insert(1,200)
print(a)

#removing elements from the numbersst
a=[50,30,80,90,100,30,140,30]
a.remove(80)
print(a)

#removing elements using pop
#removes the element from the end, and returns the element that is removed
c=a.pop()  
print(c)
print(a)
a.pop(2)            #removes the element which is at index position 2
print(a)

#Sorting
a=[50,30,80,90,100,30,140,30]
a.sort()                      #by default sorts in ascending order
print(a)

a.reverse()                   #reverses the numbers
print(a)
#Sorting in descending
b=[5,1,2,310,80,60]
b.sort(reverse=True)
print(b)

#Finding the position of an element
fruits=['apple','pear','grapes','orange']
print(fruits.index('grapes'))

#count of number of times 'pear' has been repeated in 'fruits'
print(fruits.count('pear'))
