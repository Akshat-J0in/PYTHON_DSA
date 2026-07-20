"""
Problem Statement:
Given the head of a doubly linked list with its values sorted in non-decreasing order.
Remove all duplicate occurrences of any value in the list so that only distinct values are present in the list.
Return the head of the modified linked list.
"""


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None
    
class Solution:
    def __init__(self):
        self.head = None

    def insert_node(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            return
        
        current = self.head

        while current.next:
            current = current.next
        
        current.next = newNode
        newNode.prev = current
    
    def remove_duplicates(self):
        if not self.head:
            return None
        
        current = self.head

        while current and current.next:
            nextDistinct = current.next

            while nextDistinct and nextDistinct.data == current.data:
                nextDistinct = nextDistinct.next
            
            current.next = nextDistinct
            if nextDistinct:
                nextDistinct.prev = current
            
            current = current.next
        
        return self.head
    
    def printList(self):
        current = self.head

        while current:
            print(current.data, end=' ')
            current = current.next
        print()

if __name__ == "__main__":
    sol = Solution()

    values = [1,2,2,2,3,4,4,5,5,6]

    for value in values:
        sol.insert_node(value)
    
    print("Original List")
    sol.printList()

    sol.remove_duplicates()

    print("After removing duplicates:")
    sol.printList()

