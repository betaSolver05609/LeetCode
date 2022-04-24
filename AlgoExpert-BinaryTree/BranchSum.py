# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	sums=[];
	p=calculateSum(root, 0, sums);
	return p;


def calculateSum(root, temp, sums=[]):
	# if root!=None:
	# 	print(root.data, temp);
	# 	if root.data==29:
	# 		print(root.left.data);
	if root==None:
		return sums;
	if root.left==None and root.right==None:
		# print("leaf node detected", root.data);
		temp=temp+root.value
		sums.append(temp);
		temp=0;
	else:
		temp=temp+root.value;
	calculateSum(root.left, temp, sums);
	calculateSum(root.right, temp, sums);
	return sums;