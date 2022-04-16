# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:21:10 2022

@author: Dell inspiron
"""

class Node:
    def __init__(self, data):
        self.data=data;
        self.left=None;
        self.right=None
        

def insert_into_tree(data, root):
    if root==None:
        root.data=data;
        root.left=None;
        root.right=None;
    elif data<root.data:
        if root.left==None:
            root.left=Node(data);
        else:
            insert_into_tree(data, root.left)
    else:
        if root.right==None:
            root.right=Node(data);
        else:
            insert_into_tree(data, root.right)


tree=Node(27);

insert_into_tree(25, tree)
insert_into_tree(14, tree)
insert_into_tree(26, tree)
insert_into_tree(30, tree)
insert_into_tree(29, tree)
insert_into_tree(28, tree)

def level_order_traversal(tree):
    q=list();
    q.append(tree);
    traversal_seq=[];
    while len(q)!=0:
        elem=q.pop(0);
        traversal_seq.append(elem.data)
        if elem.left!= None:
            q.append(elem.left)
        if elem.right!= None:
            q.append(elem.right);
    print('Level Order Traversal Sequence:- ', traversal_seq)

#level_order_traversal(tree);

#Find Maximum element in a binary tree?

#Even though the insertion process is BST, we will treat it as a binary tree

def maximumElement(tree):
    q=list();
    q.append(tree);
    maximum=tree.data
    while len(q)!=0:
        elem=q.pop(0);
        if elem.data>maximum:
            maximum=elem.data;
        if elem.left!= None:
            q.append(elem.left)
        if elem.right!= None:
            q.append(elem.right);
    return maximum;


#Find an element in a binary tree

#With Recursion:

def searchWithRecursion(tree, data):
    if tree==None:
        return False;
    elif tree.data==data:
        return True;
    else:
        temp=searchWithRecursion(tree.left, data);
        if temp==True:
            return temp;
        else:
            return searchWithRecursion(tree.right, data);

#Without Recursion

def searchWithoutRecursion(tree, data):
    q=list();
    q.append(tree);
    while len(q)!=0:
        elem=q.pop(0);
        if elem.data==data:
            return True;
        if elem.left!= None:
            q.append(elem.left)
        if elem.right!= None:
            q.append(elem.right);
    return False;

#Size of an BT: Simply mean the number of nodes in a tree

def sizeOfBT(tree):
    if tree==None:
        return 0;
    else:
        return sizeOfBT(tree.left)+1+sizeOfBT(tree.right)

#Print level order traversal in reverse order

def level_order_traversal_reverse(tree):
    q=list();
    q.append(tree);
    stack=list();
    while len(q)!=0:
        elem=q.pop(0);
        stack.append(elem.data);
        if elem.left!= None:
            q.append(elem.left)
        if elem.right!= None:
            q.append(elem.right);
    while len(stack)!=0:
        q.append(stack.pop())
    return q;

print (level_order_traversal_reverse(tree));
        

#Height of a B







    
    


            

