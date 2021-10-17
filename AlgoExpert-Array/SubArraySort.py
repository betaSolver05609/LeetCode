#Subarray Sort

def subarraySort(array):
    # Write your code here.
	minOutOfOrder=float("inf")
	maxOutOfOrder=float("-inf")
	for i in range(len(array)):
		num=array[i]
		if outOfOrder(i, num, array):
			minOutOfOrder=min(minOutOfOrder, num)
			maxOutOfOrder=max(maxOutOfOrder, num)
	if minOutOfOrder==float("inf"):
		return [-1, -1]
	leftIndex=0
	while minOutOfOrder>=array[leftIndex]:
		leftIndex+=1
	rightIndex=len(array)-1
	while maxOutOfOrder<=array[rightIndex]:
		rightIndex-=1
	return [leftIndex, rightIndex]


def outOfOrder(i, num, array):
	if i==0:
		return num>array[i+1]
	if i==len(array)-1:
		return num<array[i-1]
	return num>array[i+1] or num<array[i-1]
