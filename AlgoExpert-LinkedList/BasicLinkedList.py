class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        

class LinkedList:
    def __init__(self):
        self.head=None


ll=LinkedList();

def insert_element(array):
    p=Node(array[0])
    ll.head=p
    for i in range(1, len(array)):
        p.next=Node(array[i])
        p=p.next

def print_list():
    temp=ll.head
    while temp:
        print(temp.data)
        temp=temp.next


insert_element([1,2,3,4,5,6,7,8,9]);
print_list();
