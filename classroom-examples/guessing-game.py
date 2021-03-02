import random

GUESS = random.randint(1,1000)

while True:
	myguess = int(input("Enter a number : "))
	if myguess > GUESS:
		print("Enter a smaller number")
	elif myguess < GUESS:
		print("Enter a larger number")
	else:
		print("Your guess is correct")
		break


#Come back by 2:30 pm.