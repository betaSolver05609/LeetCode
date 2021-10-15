#Sorted Square Array

def sortedSquaredArray(array):
	sortedArray=[0 for i in array]
	firstPointer=0
	lastPointer=len(array)-1
	for i in reversed(range(len(array))):
		smallestNumber=array[firstPointer]
		largestNumber=array[lastPointer]
		if abs(smallestNumber)>abs(largestNumber):
			sortedArray[i]=smallestNumber**2
			firstPointer+=1
		else:
			sortedArray[i]=largestNumber**2
			lastPointer-=1
	return sortedArray
		
		
#JavaScript

function sortedSquaredArray(array) {
  sortedArray=new Array(array.length)
	firstPointer=0
	lastPointer=array.length-1
	for(let i=array.length-1; i>=0;i--){
		smallestNumber=array[firstPointer]
		largestNumber=array[lastPointer]
		if(Math.abs(array[firstPointer])>Math.abs(array[lastPointer])){
			sortedArray[i]=array[firstPointer]*array[firstPointer]
			firstPointer++;
		}
		else{
			sortedArray[i]=array[lastPointer]*array[lastPointer]
			lastPointer--;
		}
	}
	return sortedArray
}

// Do not edit the line below.
exports.sortedSquaredArray = sortedSquaredArray;
