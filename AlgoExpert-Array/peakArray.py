#Longest Peak in array

def longestPeak(array):
    # Write your code here.
	i=1
	longestPeakLength=0
	while i<len(array)-1:
		isPeak=array[i-1]<array[i] and array[i]>array[i+1]
		if not isPeak:
			i+=1
			continue
		left=i-2
		while left>=0 and array[left]<array[left+1]:
			left=left-1
		right=i+2
		while right<len(array) and array[right]<array[right-1]:
			right=right+1
		currentPeakLength=right-left-1
		longestPeakLength=max(currentPeakLength, longestPeakLength)
		i=right;
	return longestPeakLength
