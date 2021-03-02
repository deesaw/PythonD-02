try:
	amount =  int(input("Enter the amount you wish to withdraw."))
except ValueError:
	print("Please enter a valid amount")
else:
	print("Please collect your cash")