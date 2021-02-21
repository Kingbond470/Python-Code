'''
searching element in array 
python has inbuild function to do 
if element in array:
	print array.index(element)

Implementing search in linear search
start from left most element of array and compare with it each element of array -----> if element matches with other element, return the index otherwise ------> return -1

'''
def linear_search(array,x):
	for i in range(len(array)):
		if array[i]==x:
			return i
	return -1
array=['a','b','c','d','e']
x='e'
print("the element index position is "+str(linear_search(array,x)))