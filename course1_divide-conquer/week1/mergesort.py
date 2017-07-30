def merge(arr,l,m,r):
	# #Make softcopies of the array into left and right arrays
	n1 = m-l+1 #+1 to include index m, and total length is r-l+1, since array starts from index 0.
	n2 = r-m
	left_arr = []
	right_arr = []
	for i in range(0,n1):
		left_arr.append(arr[l+i])
	for j in range(0,n2):
		right_arr.append(arr[m+1+j])

	#Initialize number of elements and indexes
	i = 0
	j = 0
	k = l

	while (i<n1 and j<n2):
		if(left_arr[i]>right_arr[j]):
			arr[k] = right_arr[j]
			j+=1
			k+=1
		else:
			arr[k] = left_arr[i]
			i+=1
			k+=1
	#When there are still leftovers
	while (i<n1):
		arr[k] = left_arr[i]
		i+=1
		k+=1

	while (j<n2):
		arr[k] = right_arr[j]
		j+=1
		k+=1

def mergesort(arr, l, r):
	if (l<r):
		m = l+(r-l)/2 #Can use (l+r)/2
		mergesort(arr,l,m)
		mergesort(arr,m+1,r)
		merge(arr,l,m,r)

# Testcase
arr = [99, 77, 66, 55, 55, 111, 88, 0, -77]
n = len(arr)
print ("Original array:")
for i in range(n):
    print ("%d" %arr[i]), 
    # %d : Signed integer decimal
    # puts ' at the end to print in horizontal
 
mergesort(arr,0,n-1)
print ("\nSorted array:")
for i in range(n):
    print ("%d" %arr[i]),

# mergesort(arr,2,n-3)
# print ("\nSorted array (from index 2 to last index-2:")
# for i in range(n):
#     print ("%d" %arr[i]),