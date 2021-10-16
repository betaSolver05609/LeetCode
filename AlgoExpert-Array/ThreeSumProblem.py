#Three Sum Solution

#optimal solution

def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort();
	a=[]
	for i in range(len(array)-1):
		left=i+1
		right=len(array)-1
		while left<right:
			currentSum=array[left]+array[right]+array[i]
			if currentSum==targetSum:
				a.append([array[i], array[left], array[right]])
				print(array[i], a)
				left+=1;
				right-=1
			elif currentSum>targetSum:
				right-=1
			elif currentSum<targetSum:
				left+=1
	return a
		
		



#Three pass Solution

#As a subproblem of 2 pass Solution

def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort();
	a=[]
	for i in range(len(array)):
		numToSearch=targetSum-array[i]
		p=twoPassSolution(array[i+1:len(array)], numToSearch)
		if len(p)!=0:
			for elem in p:
				elem.insert(0, array[i])
				a.append(elem)
    return a

def twoPassSolution(array, target):
	map={}
	a=[]
	if len(array)==0:
		return [];
	if len(array)==1:
		return []
	if len(array)==2:
		print("Entered here", array)
		if sum(array)==target:
			return [array]
		else:
			return []
	for i in range(len(array)):
		numToSearch=target-array[i]
		print(map)
		if numToSearch in map:
			if numToSearch>array[i]:
				a.append([array[i], numToSearch])
			else:
				a.append([numToSearch, array[i]])
		map[array[i]]=i
	return a
