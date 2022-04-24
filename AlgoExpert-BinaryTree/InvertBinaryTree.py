def invertBinaryTree(tree):
    # Write your code here.
    temp=tree;
    invert(temp);
    return temp;

def invertRecursive(root):
    if root is None:
        return;
    if root.left is not None and root.right is not None:
        temp=root.left
        root.left=root.right;
        root.right=temp;
    elif root.right is not None and root.left is None:
        root.left=root.right;
        root.right=None;
    else:
        root.right=root.left;
        root.left=None;
    invert(root.left);
    invert(root.right);


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
