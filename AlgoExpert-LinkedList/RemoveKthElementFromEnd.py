# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	pos=1
	kthNode=head
	while pos!=k:
		kthNode=kthNode.next
		pos+=1
	
	if kthNode.next==None or kthNode==None:
		head.value=head.next.value
		head.next=head.next.next
		return
	temp=head
	prev=None
	while kthNode:
		if kthNode.next==None:
			break
		prev=temp
		temp=temp.next
		kthNode=kthNode.next
	#print(prev.value, temp.value)
	prev.next=temp.next
    pass
