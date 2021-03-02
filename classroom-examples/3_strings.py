#String Operators
fruit = "Apple"
colour = "red"
taste = "i love green Apples, they are tasty"
print(colour + fruit)                              # Concatenation
print(fruit * 3)                                   # repetition

#String methods
print(fruit.lower())
print(fruit.upper())
print(taste.capitalize())        #capitalizes the first letter 
print(taste.title())             #capitalizes the first letter in each word
print(taste.swapcase())          #converts lower to upper and vice versa
print(taste.count('a'))          #counts 

#membership operators
print('pp' in fruit)
print('green' not in taste)
