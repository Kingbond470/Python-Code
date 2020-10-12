print('please think of a number between 1 and 100  ' )
high=100
low=0
guess=int((low+high)/2.0)
while True:
	print('is your secret number ' +str(guess)+' ?')
	user_input=input("Enter 'h' to show that our guess is higher than yours. "+"Enter 'l' to show that our guess is lower than yours. "+"Enter 'c' to show that our guess is correct. \n ")
	if user_input =='h':
		high=guess
		guess=(low+high)/2
	elif user_input=='l':
		low=guess
		guess=(low+high)/2
	elif user_input=='c':
		break
	else:
		print("Hmm....I did not understand your input")
print("GAME OVER! your secret number was "+str(guess))		