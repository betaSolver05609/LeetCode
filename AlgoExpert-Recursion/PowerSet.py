#Power Set

def powerset(array, index=None):
    # Write your code here.
	if index is None:
		index=len(array)-1
	if index<0:
		return [[]]
	else:
		element=array[index]
		subsets=powerset(array, index-1)
		for i in range(len(subsets)):
			current=subsets[i]
			subsets.append(current + [element])
	return subsets

#Aiterative solution

def powerset(array):
    # Write your code here.
	powerArray=[[]]
	for i in range(len(array)):
		for j in range(len(powerArray)):
			current=powerArray[j]
			powerArray.append(current+[array[i]])
			print(powerArray)
		print("-------------------")
    print(powerArray)
	return powerArray
