def powerRecurrence(base,exp):
	if exp==0:
		return 1
	else:
		return base*powerRecurrence(base,exp-1)
base=int(input("enter the base value: "))
exp=int(input("enter the exponent value: "))
print("The value is "+str(powerRecurrence(base,exp)))