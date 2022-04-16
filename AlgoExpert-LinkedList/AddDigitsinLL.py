# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
	newListHead=LinkedList(0);
	
	temp1=linkedListOne
	temp2=linkedListTwo
	temp3=newListHead
	carry=0
	prevListNode=None
	while temp1 or temp2:
		if temp1 is not None and temp2 is None:
			s=temp1.value+carry
			val=s%10
			carry=s//10
			print(temp1.value, carry, val)
			temp3.value=val
			temp3.next=LinkedList(0);
			prev=temp3
			temp1=temp1.next
			temp3=temp3.next
		elif temp1 is None and temp2 is not None:
			s=temp2.value+carry
			val=s%10
			carry=s//10
			temp3.value=val
			temp3.next=LinkedList(0);
			prev=temp3
			temp2=temp2.next
			temp3=temp3.next
		else:
			s=temp1.value+temp2.value+carry
			val=s%10
			carry=s//10
			#print(temp1.value, temp2.value, val,carry)
			temp3.value=val
			temp3.next=LinkedList(0);
			prev=temp3
			temp3=temp3.next
			temp1=temp1.next
			temp2=temp2.next
	if carry==0:
		prev.next=None
	else:
		prev.next=LinkedList(carry)
	return newListHead
