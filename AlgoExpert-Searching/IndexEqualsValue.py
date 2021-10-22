def indexEqualsValue(array):
    # Write your code here.
	return indexHelper(array)


def indexHelper(array):
	left=0
	right=len(array)-1
	while left<=right:
		middle=(left+right)//2
		target=middle
		if target>array[middle]:
			left=middle+1
		elif array[middle]==middle and middle==0:
			return middle
		elif array[middle]==middle and array[middle-1]<middle-1:
			return middle
		else:
			right=middle-1
	return -1