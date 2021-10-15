//Valid Subsequnce

// 1Pass Solution O(n)

//JS

function isValidSubsequence(array, sequence) {
  // Write your code here.
	let j=0;
	let lastIndex=0;
	for(let i=0;i<array.length;i++){
		if(sequence[j]===array[i] && i>=lastIndex){
			j++;
			lastIndex=i
		}
		else if(sequence[j]===array[i] && i<lastIndex)
			return false;
	}
	if(j!==sequence.length)
		return false
	return true
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;


//Python
def isValidSubsequence(array, sequence):
    # Write your code here.
	j=0;
	lastIndex=0;
	try:
    	for i in range(len(array)):
			print(j, len(sequence))
			if j==len(sequence):
				return True
			if sequence[j]==array[i] and lastIndex<=i:
				j=j+1;
				lastIndex=i
			elif sequence[j]==array[i] and lastIndex>i:
				return False
	except:
		print("Entering Except")
		return False
	if j==len(sequence):
		return True
	return False
