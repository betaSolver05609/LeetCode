# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Write your code here.
	HashMap={}
	temp=head
	while temp:
		if temp in HashMap:
			return temp
		else:
			HashMap[temp]=temp.value
		temp=temp.next
	return
