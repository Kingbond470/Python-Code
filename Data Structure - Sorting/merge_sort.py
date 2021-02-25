'''
Merge Sort is a Divide & Conquer principle based algorithm, like  its cousin Quick  Sort. The main idea of merge sort is to divide large data-sets into smaller sets of data, and then solve them. Merge Sort is a recursive algorithm, it divides the given array into smaller half’s and then calls itself repeatedly to solve them.
'''

# first sub array is arr[l....m] and second sub array is arr[m+1...r]
def merge(arr,l,m,r):
	n1=m-l+1
	n2=r-m
	# creating new two array as temp
	L=[0]*(n1)
	R=[0]*(n2)
	#copying data to temp arrays L and R
	for i in range(0,n1):
		L[i]=arr[l+i]
	for j in range(0,n2):
		R[j]=arr[m+1+j]
	#merge the temp arrays into arr[l...r]
	#initial index of i and j is zero and k is initial index of merged subarray 
	i=0
	j=0
	k=l
	#copy the remaining element into L and R if there are any left
	while i<n1 and j<n2:
		if L[i]<=R[j]:
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1
		k+=1
	while i<n1:
		arr[k]=L[i]
		i+=1
		k+=1
	while j<n2:
		arr[k]=R[j]
		j+=1
		k+=1
# l and r is left and right index and sub array of arr to be sorted
def merge_sort(arr,l,r):
	if l<r:
		m=(l+(r-1))//2
		#first and second halves
		merge_sort(arr,l,m)
		merge_sort(arr,m+1,r)
		merge(arr,l,m,r)
arr=[47,56,87,9,8,6,34,95,23,45]
n=len(arr)
print("given array is")
for i in range(n):
	print("%d" %arr[i])
merge_sort(arr,0,n-1)
print("sorted array is")
for i in range(n):
	print("%d"  %arr[i])