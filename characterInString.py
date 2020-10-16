'''
character: a single character
string: an alphabet string
returns : true if char is in string otherwise false
'''
def charinstring(char,string):
	if string == '':
		return False
	mid=len(string)/2
	if string[mid] == char:
		return True
	elif string[mid] < char:
		return charinstring(char,string[mid+1:])
	elif string[mid] > char:
		return charinstring(char,string[:mid])
string=input("enter the string: ")
char=input("enter the character: ")
print(charinstring(char,string))