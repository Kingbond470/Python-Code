'''
string: a string (char+number+space)
returns: int, length of string
'''
def lenofstring(string):
	count=0
	for dummy_count in string:
		count+=1
	return count
string=input('enter the string of your choice: ')
print("Total length  of string: "+str(lenofstring(string)))