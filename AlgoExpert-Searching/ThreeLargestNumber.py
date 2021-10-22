def findThreeLargestNumbers(array):
    # Write your code here.
	max1=float("-inf")
	max2=float("-inf")
	max3=float("-inf")
	
	for i in range(len(array)):
		if array[i]>=max1:
			print("max1", array[i])
			max3=max2
			max2=max1
			max1=array[i]
		if array[i]<max1 and array[i]>=max2:
			print("max2", array[i])
			max3=max2
			max2=array[i]
		if array[i]<max2 and array[i]>=max3:
			print("max3", array[i])
			max3=array[i]
	print([max3, max2, max1])
    return [max3, max2, max1]