#Recursive

def shiftedBinarySearch(array, target):
    # Write your code here.
	return binaryhelper(array, target, 0, len(array)-1)
    pass

def binaryhelper(array, target, left, right):
	
	if left>right:
		return -1
	middle=(left+right)//2
	leftNum=array[left]
	rightNum=array[right]
	if array[middle]==target:
		return middle
	
	if leftNum<=array[middle]:
		if target>=leftNum and target<array[middle]:
			return binaryhelper(array, target, left, middle-1)
		else:
			return binaryhelper(array, target, middle+1, right)
	else:
		if target<rightNum and target>array[middle]:
			return binaryhelper(array, target, middle+1, right)
		else:
			return binaryhelper(array, target, left, middle-1)
		
		
	

#Iterative

def shiftedBinarySearch(array, target):
    # Write your code here.
	return binaryhelper(array, target, 0, len(array)-1)
    pass

def binaryhelper(array, target, left, right):
	while left<=right:
		middle=(left+right)//2
		leftNum=array[left]
		rightNum=array[right]
		potentialMatch=array[middle]
		if target==potentialMatch:
			return middle
		if leftNum<=potentialMatch:
			if target>=leftNum and target<potentialMatch:
				right=middle-1
			else:
				left=middle+1
		else:
			if target>=potentialMatch and target<rightNum:
				left=middle+1
			else:
				right=middle-1
	return -1
