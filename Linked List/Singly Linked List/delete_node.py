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