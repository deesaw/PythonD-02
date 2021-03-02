#Strings
word='hello'
sentence="Welcome to Python World"
para="""Good morning
how are you doing 
today"""

#input() function is used to read a string from standard input such as keyboard.
name = input("Enter your name: ")
print(name)
print (len(name))
print (type(name))

#Python index starts from 0

text = "Its healthy to have vegetables"
print(text)
#Indexing
print(text[0])						#prints the first character
print(text[4])						#prints the 5th character
print(text[-1])						#prints the last character
# Slicing
print(text[4:10])                   # Range slicing
print(text[:10])
print(text[2:])
print(text[:])

print(text[0:10:2])
print(text[0::2])                    #prints every second character
print(text[::1])
print(text[-1])                      #prints the last character
print(text[::-1])                    #reverse the string
print(text[-2:])                     #prints last two characters    
