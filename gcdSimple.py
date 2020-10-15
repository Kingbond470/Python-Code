'''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
'''
def gcdSimple(a,b):
	if b==0:
		return a
	else:
		return gcdSimple(b,a%b)
a=int(input( "enter the value of a:"))
b=int (input("enter the value of b:"))
print(gcdSimple(a,b))