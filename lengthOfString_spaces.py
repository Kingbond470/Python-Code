'''
string : a string with number and char,spaces
returns :int,length of a string
'''
def lengthofstring(string):
	if string=='':
		return  0
	else:
		return 1+lengthofstring(string[:-1])
string=input("enter the string: ")
print("Total length of string: ",str(lengthofstring(string)))