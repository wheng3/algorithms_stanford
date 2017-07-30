def count_split_inv(arr1, arr2):
	temp =[]
	count = 0
	while arr1 and arr2: #while both arrays have elements
		if(arr1[0]>arr2[0]):
			temp.append(arr2.pop(0))
			count += len(arr1)
		else:
			temp.append(arr1.pop(0))

	temp += arr1+arr2 #handle the leftovers

	return temp, count

def sortcount(arr):
	n = len(arr)
	if (n==1):
		return arr, 0
	else:
		m = n/2
		arr1 = arr[:m]
		arr2 = arr[m:]
		arr1, half1= sortcount(arr1)
		arr2, half2 = sortcount(arr2)
		arrfull, full = count_split_inv(arr1, arr2)
		return arrfull, half1+half2+full

# Testcase
arr = [77, 0, 77, 1, 7, 99, 3, -50, 3, 4, 5, 55]
n = len(arr)
print ("Original array:")
for i in range(n):
    print ("%d" %arr[i]), 

arr, count = sortcount(arr)
print ("\nSorted array:")
for i in range(n):
    print ("%d" %arr[i]),

print("\nNumber of inversions are:"),
print count
