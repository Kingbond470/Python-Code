'''
Selection Sort is a technique where a array is sequentially sorted by placing the smallest or the largest element from the array one after the other in multiple iterations. The time complexity of selection sort is more  then the time complexity of insertion sort. Algorithm is not suitable for large data sets.
'''
import sys
a=[67,84,6,9,8,7]

for i in range(len(a)):
	min_idx=i				#finding the min element in remaining unsorted array
	for j in range(i+1,len(a)):
		if a[min_idx]>a[j]:
			min_idx=j
	a[i],a[min_idx]=a[min_idx],a[i] 		#swaping the min element with first element
print("the sorted array is")
for i in range(len(a)):
	print("%d" %a[i])
		