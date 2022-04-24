# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
	print(solve(tree, node));

def solve(node, value):
    stack=[]
    while node.left is not None: 
        if node.left.value==value:
            return node.left;
        else:
            stack.append(node);
        node=node.left
    while len(stack):
        node=stack.pop();
        if node.right.value==value:
            return node.parent;
    return 0;

