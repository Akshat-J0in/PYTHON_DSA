"""
What is Linked List?
Linked list is a linear data structure that can be visualized as a chain with different nodes connecte,
Where each nodes represents different element. The difference between arrays and linked list is that, unlike
arrays, linked list does not store elements in contiguous memory locations.
A Linked list is a data structure containing 2 information, the first being the data and the other being
the pointer to the next element. The 'head' is the first node and the 'tail' is the last node in a linked list.
"""

# Creating a node in a linked list

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

arr = [2,5,8,7]
y = Node(arr[0])

print(y)
print(y.data)