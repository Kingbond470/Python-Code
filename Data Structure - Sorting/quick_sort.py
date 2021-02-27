'''
Quick sort is a sorting algorithm, used in data structures for sorting arrays, queues, linked lists and other linear data structures. Quick sort works on the principle of Divide and Conquer. Quick sort is also known as partition-exchange sort.
step-
 There are many different versions of quickSort that pick pivot in different ways. 

    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.

/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[p] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

'''
# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 


def partition(arr, low, high): 
	i = (low-1)		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low, high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 

			# increment index of smaller element 
			i = i+1
			arr[i], arr[j] = arr[j], arr[i] 

	arr[i+1], arr[high] = arr[high], arr[i+1] 
	return (i+1) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

def quickSort(arr, low, high): 
	if len(arr) == 1: 
		return arr 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr, low, high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
print("the given array is")
for i in range(n):
	print("%d" %arr[i])
quickSort(arr, 0, n-1) 
print("Sorted array is:") 
for i in range(n): 
	print("%d" % arr[i])
