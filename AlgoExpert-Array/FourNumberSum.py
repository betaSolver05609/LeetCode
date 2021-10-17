#Four Number Sum
#Space O(n2)
#Time Average O(n2) and Worst O(n3)

def fourNumberSum(array, targetSum):
    # Write your code here.
	quad=[]
	HashMap={}
	
	for i in range(1, len(array)):
		for j in range(i+1, len(array)):
			currentSum=array[i]+array[j]
			difference=targetSum-currentSum
			if difference in HashMap:
				for pair in HashMap[difference]:
					quad.append(pair + [array[i], array[j]])
		for k in range(0,i):
			currentSum=array[i]+array[k]
			if currentSum in HashMap:
				HashMap[currentSum].append([array[i], array[k]])
			else:
				HashMap[currentSum]=[[array[i], array[k]]]
	return quad

