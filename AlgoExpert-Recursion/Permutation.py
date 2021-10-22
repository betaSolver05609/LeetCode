

#Non optimal Solution

def getPermutations(array):
    # Write your code here.
	permutations=[]
	permutationsCreator(array, [], permutations)
	#print(permutations)
	return permutations

def permutationsCreator(array, currentPermutations, permutations):
	#print(currentPermutations)
	if not len(array) and len(currentPermutations):
		#print(array)
		permutations.append(currentPermutations)
	else:
		for i in range(len(array)):
			newArray=array[:i]+array[i+1:]
			print(newArray)
			newPermutation=currentPermutations + [array[i]]
			#print(newPermutation)
			permutationsCreator(newArray, newPermutation, permutations)

#Optimal Solution

def getPermutations(array):
    # Write yor code here.
	permutation=[]
	perm(0, array, permutation)
	print(permutation)
	return permutation


def perm(i, array, permutation):
	if i==len(array)-1:
		print(array)
		permutation.append(array)
		print(permutation)
	else:
		for j in range(i, len(array)):
			swap(array,i,j)
			perm(i+1, array, permutation)
			swap(array,i,j)

def swap(array, i, j):
	array[i], array[j]=array[j], array[i]