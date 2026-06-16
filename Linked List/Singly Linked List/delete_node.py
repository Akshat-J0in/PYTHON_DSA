# Deleting node from the start of the linked list
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class solution:
#     def delete_node(self, head):
#         if head == None or head.next == None:
#             return None
        
#         else:
#             head.data = head.next.data
#             head.next = head.next.next
#             return head


# if __name__ == "__main__":
#     head = node(10)
#     node2 = node(20)
#     node3 = node(30)
#     node4 = node(40)

#     head.next = node2
#     node2.next = node3
#     node3.next = node4

#     # list before deletion
#     temp = head
#     while temp:
#         print(temp.data, end=" ")
#         temp = temp.next
#     print()
#     obj = solution()
#     head = obj.delete_node(head)

#     # list after deletion
#     temp = head
#     while temp:
#         print(temp.data, end=' ')
#         temp = temp.next
"""
Over here we are deleting a node from the start of the linked list.
So over here first we define a class node that will create a node and make a linedlist.
then we have a class solution where we have a mentioned a condition where if the head is null or the head of next is null then we are returning null.
If this is not the case then we are making the head of data as data of head of next and the value it points to is head of next of next
"""



# Deleting node from the end of the linedlist

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def delete_node(self, head):
        if head is None or head.next is None:
            return None
        
        curr = head
        while curr.next.next is not None:
            curr = curr.next
        
        curr.next = None

        return head

if __name__ == "__main__":
    head = node(10)
    node2 = node(20)
    node3 = node(30)
    node4 = node(40)

    head.next = node2
    node2.next = node3
    node3.next = node4

    # Print before deleting
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    
    print()
    
    obj = solution()
    head = obj.delete_node(head)

    # List after deleting a node
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    """
    Over here we are deleting the tail of the linked list.
    Over here the node class remains the same.
    The solution class over here changes.
    That is if head is none or head of next is none, we will return none
    Otherwise we will go to the second last node using while loop and make the the next node of the second last node as null and then return the head.
    """