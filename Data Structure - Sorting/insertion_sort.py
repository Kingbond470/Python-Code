'''
Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

First, we consider the 0th index as sorted part and the rest is unsorted.
Then we compare the next element of the array with the first element of the array, if the first element is smaller then the second element then we swap the elements, otherwise we place the element after the first element
Thus each time we insert element the sorted array becomes larger and unsorted becomes smaller, and the new element is to be compare with all the previous elements of the sorted array and adjust the element just next to its smaller element.
'''

def insertion_sort(arr):
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j -=1
		arr[j+1]=key

arr=[30,67,87,8,9,4,6,7,34]
insertion_sort(arr)
print("sorted array is ")
for i in range(len(arr)):
	print("%d" %arr[i])