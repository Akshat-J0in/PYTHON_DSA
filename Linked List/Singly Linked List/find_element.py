"""
Problem Statement:
Given the head of a linked list and an integer value, find out whether the integer is present in the linked list or not.
Return true if it is present, or else return false.
"""



class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def is_present(self, head, key):
        curr = head
        while curr is not None:
            if curr.data == key:
                return True
            
            curr = curr.next
        return False
                

if __name__ == "__main__":
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)

    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next
    
    obj = solution()

    if obj.is_present(head, 100):
        print("Found")
    else:
        print("Not Found")
"""
This is also a simple code where we have first taken the values form the user and created a linked list then we have created another class of solution.
In this we have created a method where we have found if the element is present in the list or not. If not then we return false and if there we return true.
"""