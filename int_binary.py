x=int(input("provide an integer to us from your side "))
output =''

isNegative=x<0
x=abs(x)

if x==0:
	output='0'
while x>0:
	output=str(x%2) + output
	x/=2
if isNegative:
	output='-' + output
print("Binary represntation is: " + output)