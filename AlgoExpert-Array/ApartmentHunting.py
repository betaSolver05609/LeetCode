#Apartment Hunting

#complexity O(br) where b is no of blcoks and r is number of requirements

def apartmentHunting(blocks, reqs):
    # Write your code here.
	HashMap={}
	for req in reqs:
		HashMap[req]=findMinimumDistances(blocks, req)
	blockIndex=findMinBlockIndex(HashMap, reqs, blocks)
	print(HashMap)
    return blockIndex

def findMinBlockIndex(HashMap, reqs, blocks):
	minBlock=[]
	mindist=[0 for block in blocks]
	for req in reqs:
		minBlock.append(HashMap[req])
	for i in range(len(mindist)):
		values=[]
		for req in reqs:
			values.append(HashMap[req][i])
		mindist[i]=max(values)
	a=min(mindist)
	idx=mindist.index(a)
	print(mindist)
	return idx
			
def findMinimumDistances(blocks, req):
	mindist=[0 for block in blocks]
	closestIdx=float("inf")
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestIdx=i
		mindist[i]=distanceBetween(i, closestIdx)
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestIdx=i
		mindist[i]=min(mindist[i], distanceBetween(i, closestIdx))
	return mindist

		
def distanceBetween(a,b):
	return abs(a-b)
	