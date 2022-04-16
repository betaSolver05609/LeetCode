# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
	temp=head.next
	prev=head
	prev.next=None
	while temp:
		nex=temp.next
		temp.next=prev
		prev=temp
		temp=nex
	head=prev
	print(head.value)
    return head
