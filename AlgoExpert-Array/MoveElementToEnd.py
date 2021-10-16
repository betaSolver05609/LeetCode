#Move Element to End

#Also optimal solution. Linear time O(n)

def moveElementToEnd(array, toMove):
    # Write your code here.
    pointer=len(array)-1;
	for i in reversed(range(len(array)-1)):
		if array[pointer]==toMove:
			pointer-=1
		if array[i]==toMove:
			array[pointer], array[i]=array[i], array[pointer]
	print(array)
	return array
		
