def nodeDepths(root):
    # Write your code here.
    print(nodeDepth(root, 0, 0));
    return nodeDepth(root, 0,0);



#Recursive Solution:

def nodeDepthRecursive(root, depth):
    if root is None:
        return 0;
    return depth+nodeDepth(root.left, depth+1)+nodeDepth(root.right, depth+1);

   


def nodeDepth(root, temp=0, s=0):
    queue=[]
    s=0;
    queue.append({'node': root, 'depth': 0});
    while len(queue):
        node=queue.pop(0);
        s=s+node['depth'];
        temp=node['depth']
        if node['node'].left is not None:
            queue.append({'node': node['node'].left, 'depth': temp+1});
        if node['node'].right is not None:
            queue.append({'node': node['node'].right, 'depth': temp+1});
    return s;



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
