#First Duplicate Value

#O(n) time and O(1) solution

#This Solution will only work if it is guarenteed that numbers in array
#will always be between 1 and n where n is the length of the array

def firstDuplicateValue(array):
    # Write your code here.
	for value in array:
		absValue=abs(value)
		if array[absValue-1]<0:
			return value
		else:
			array[absValue-1]*=-1
    return []




#My Solution
#Time complexity O(n)

def firstDuplicateValue(array):
    # Write your code here.
	HashMap={}
	for i in range(len(array)):
		if array[i] in HashMap:
			return array[i]
		else:
			HashMap[array[i]]=i
	return -1