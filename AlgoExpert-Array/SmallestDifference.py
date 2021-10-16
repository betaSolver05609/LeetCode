#Optimal Solution O(nlogn + mlogm + max(n,m))

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort();
	arrayTwo.sort();
	firstPointer=0
	secondPointer=0
	smallestPair=[]
	k=arrayOne[firstPointer]-arrayTwo[secondPointer]
	while firstPointer<len(arrayOne) and secondPointer<len(arrayTwo):
		if arrayOne[firstPointer]==arrayTwo[secondPointer]:
			smallestPair=[arrayOne[firstPointer], arrayTwo[secondPointer]]
			break;
		currentDifference=arrayOne[firstPointer]-arrayTwo[secondPointer]
		if abs(currentDifference)<abs(k):
			k=currentDifference
			smallestPair=[arrayOne[firstPointer], arrayTwo[secondPointer]]
		if arrayOne[firstPointer]>arrayTwo[secondPointer]:
			secondPointer+=1
		elif arrayOne[firstPointer]<arrayTwo[secondPointer]:
			firstPointer+=1
	return smallestPair


#Brute Force Solution O(n^2)

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    k=abs(arrayOne[0]-arrayTwo[0])
	firstElement=0
	secondElement=0
	for i in range(len(arrayOne)):
		for j in range(len(arrayTwo)):
			if abs(arrayOne[i]-arrayTwo[j])<k:
				k=abs(arrayOne[i]-arrayTwo[j])
				firstElement=arrayOne[i]
				secondElement=arrayTwo[j]
				
	return [firstElement, secondElement]
				
