#Spiral Traversal

def spiralTraverse(array):
    # Write your code here.
	result=[]
	startRow=0
	startCol=0
	endRow=len(array)-1
	endCol=len(array[0])-1
	while startRow<=endRow and startCol<=endCol:
		for col in range(startCol, endCol+1):
			print(col)
			result.append(array[startRow][col])
		for row in range(startRow+1, endRow+1):
			print(row)
			result.append(array[row][endCol])
		for col in reversed(range(startCol, endCol)):
			print(col)
			if startRow==endRow:
				break
			result.append(array[endRow][col])
		for row in reversed(range(startRow+1, endRow)):
			print(row)
			if startCol==endCol:
				break
			result.append(array[row][startCol])
		startRow+=1
		endRow-=1
		startCol+=1
		endCol-=1
	print(result)
	return result
