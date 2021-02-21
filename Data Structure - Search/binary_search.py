'''
Binary Search in Python
It is based upon the divide and conquer rule and in this searching technique sorted array is divided into two qual parts and then same technique is applied into other two halves for seaching  for element by comparing low and high.
 time and space complexit - O(1) & O(1) 
avg ---> O(log n )
worst --> O(log n)
step --> find the middle index of array--> if middle element is equal to search element stop searching ---> if element is less than middle element then consider the first half as separate array and search in it ----> if element is greater than middle element then consider the second half as separate array and search in it.---> repeat the step until we get the result.
'''

def binary_search(arr, low, high,x):
	if high>=low:
		mid=(high+low)//2
		if arr[mid]==x:
			return mid
		elif arr[mid]>x:
			return binary_search(arr, low, mid-1, x)
		else:
			return binary_search(arr, mid+1, high, x)
	else:
		return -1

arr=[2,3,4,5,6,7]
x=3
search_result=binary_search(arr,0,len(arr)-1,x)
if search_result !=-1:
	print("the element is present at index",str(search_result))
else:
	print("element is not present")