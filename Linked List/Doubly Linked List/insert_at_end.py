"""
Problem Statement:
Given a Doubly Linked List, and a value k, insert a node having bac value 'k' at the end of the doubly lined list.
"""



class Node:
    def __init__(self, data, next = None, back = None):
        self.data = data
        self.next = next
        self.back = back

def convertArr2DLL(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp
    
    return head

def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def insertAtTail(head, key):
    NewNode = Node(key)

    if not head:
        return NewNode
    
    tail = head

    while tail.next:
        tail = tail.next
    
    tail.next = NewNode
    NewNode.back = tail

    return head

if __name__ == "__main__":
    arr = [12,5,8,7,4]
    head = convertArr2DLL(arr)
    printList(head)

    head = insertAtTail(head, 10)
    printList(head)