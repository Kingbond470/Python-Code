'''
Return true if the two words are reverse of each other
parameter:str1,str2(alphabet or integer)
return
condition----a single length can not be semordnilap and equal string too
 
'''

def semordnilapWrapper(str1,str2):
	if len(str1)==1 or len(str2)==1:
		return False
	if str1==str2:
		return False
	return semordnilap(str1,str2)
def semordnilap(str1,str2):
	if len(str1)!=len(str2):
		return False
	if len(str1)==1 and len(str2)==1:
		return str1==str2
	if str1[0]==str2[-1]:
		return semordnilap(str1[1:],str2[:-1])
str1=input("enter the first string: ")
str2=input("enter the next string: ")
print("The Word "+str1+" , " +str2+" are "+str(semordnilapWrapper(str1,str2))+" reverse of each other")