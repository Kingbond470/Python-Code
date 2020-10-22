'''
give a  integer and it will returns the number of digits in a intege
parameter: ant intege(+ve or -ve)
return:number of digits in x
'''
def intDigits(x):
	x=abs(x)
	if x<10:
		return 1
	else:
		return 1+intDigits(x/10)
x=int(input("enter the integer: "))
print("Total no of digits in an integer: "+str(intDigits(x)))
