x=int(input("enter the integer: "))
for answer in range(abs(x)+1):
	if answer**3==x:
		break
if answer**3 !=abs(x):
	print(str(x)+" is not a perfect cube.")
else:
	if x<0:
		answer=- answer
	print("the cube root of " +str(x)+' is '+str(answer))