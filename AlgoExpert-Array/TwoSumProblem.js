
//JS

//Two Pass Solution

function twoNumberSum(array, targetSum) {
  // Write your code here.
	let s=new Set(array)
	for(let i=0;i<array.length;i++){
		elementToFind=targetSum-array[i]
		if(s.has(targetSum-array[i]) && elementToFind!=array[i]){
			return [elementToFind, array[i]]
		}
	}
	return []
}

//One Pass Solution

function twoNumberSum(array, targetSum) {
  // Write your code here.
	HashMap={}
	
	for(let i=0;i<array.length;i++){
		let elementToFind=targetSum-array[i];
		console.log(HashMap, array[i], elementToFind, HashMap[elementToFind]==undefined)
		if(HashMap[elementToFind]==undefined){
			HashMap={
				...HashMap,
				[array[i]]: i
			}
		}
		else {
			return [array[i], array[HashMap[elementToFind]]]
		}
			
	}
	return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;


//Python 1 pass Solution

def twoNumberSum(array, targetSum):
    # Write your code here.
    HashMap={}
	for i in range(len(array)):
		elementToFind=targetSum-array[i]
		if elementToFind in HashMap:
			return [array[i], elementToFind]
		HashMap[array[i]]=i
	return []
