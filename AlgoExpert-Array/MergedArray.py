#Merged Intervals

#O(nlogn)

def mergeOverlappingIntervals(intervals):
    # Write your code here.
	mergedArray=[]
	sortedInterval=sorted(intervals, key=lambda x:x[0])
	currentInterval=sortedInterval[0]
	mergedArray.append(currentInterval)
	
	for i in range(1, len(sortedInterval)):
		currentIntervalEnd=currentInterval[1]
		nextInterval=sortedInterval[i]
		nextIntervalStart=sortedInterval[i][0]
		nextIntervalEnd = sortedInterval[i][1]
		if currentIntervalEnd >= nextIntervalStart:
			currentInterval[1]=max(currentIntervalEnd,nextIntervalEnd)
		else:
			currentInterval=nextInterval
			mergedArray.append(currentInterval)
		
	print(mergedArray)
    return mergedArray
