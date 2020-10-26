'''
the sum of area and square of the perimeter of regualr polygon roundedd to decimal 4 places
parameter n: number of sides
parameter s: length of sides
return float
'''
import math
def polysum(n,s):
	area=(0.25*n*s**2)/(math.tan(math.pi/n))
	square_perimeter=(s*n)**2
	result_sum=area+square_perimeter
	return round(result_sum,4)
n=input('enter the number of sides:')
s=input('enter the length of side:')
print(polysum(n,s))