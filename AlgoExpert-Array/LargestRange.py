#Largest Range

def largestRange(array):
    # Write your code here.
	HashMap={}
	bestRange=[]
	longestLength=0
	for i in range(len(array)):
		HashMap[array[i]]=True
	for num in array:
		HashMap[num]=False
		currentLength=1
		left=num-1
		right=num+1
		while left in HashMap:
			HashMap[left]=False
			left=left-1
			currentLength+=1
		while right in HashMap:
			HashMap[right]=False
			right=right+1
			currentLength+=1
		if currentLength>longestLength:
			bestRange=[left+1, right-1]
			longestLength=currentLength
	return bestRange

