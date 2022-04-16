# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	currentNode=linkedList
	lastValue, lastIndex=linkedList.value, linkedList
	while currentNode:
		temp=currentNode
		if lastValue==temp.value:
			if temp.next==None:
				lastIndex.next=None
			currentNode=currentNode.next
		else:
			lastIndex.next=temp
			lastValue=temp.value
			lastIndex=lastIndex.next
			currentNode=currentNode.next
    return linkedList
