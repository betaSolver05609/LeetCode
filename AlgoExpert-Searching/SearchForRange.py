
def searchForRange(array, target):
    # Write your code here.
	leftidx=binaryhelper(array, target, 0, len(array)-1, True)
	print(leftidx)
	rightidx=binaryhelper(array, target, 0, len(array)-1, False)
	print(rightidx)
    return [leftidx, rightidx]
	pass;

def binaryhelper(array, target, left, right, goLeft):
	while left<=right:
		mid=(left+right)//2
		if target>array[mid]:
			left=mid+1
		elif target<array[mid]:
			right=mid-1
		else:
			if goLeft:
				if mid==0 or array[mid-1]!=target:
					return mid
				else:
					right=mid-1
			else:
				if mid==len(array)-1 or array[mid+1]!=target:
					return mid
				else:
					left=mid+1
	return -1
