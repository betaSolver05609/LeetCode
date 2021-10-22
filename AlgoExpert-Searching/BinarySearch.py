def binarySearch(array, target):
    # Write your code here.
	startIndex=len(array)//2
	if len(array)==0:
		return -1
	if len(array)==1 and array[0]==target:
		return 1
	while startIndex>=0 and startIndex<len(array):
		if array[startIndex]==target:
			return startIndex
		elif target<array[startIndex] and target>array[startIndex-1]:
			return -1
		elif target>array[startIndex]:
			startIndex+=1
		elif target<array[startIndex]:
			startIndex-=1
	return -1
