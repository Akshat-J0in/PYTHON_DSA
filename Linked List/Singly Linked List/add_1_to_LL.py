class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def append(self, head, value):
        new_node = Node(value)

        if not head:
            return new_node
        
        current = head

        while current.next:
            current = current.next
        current.next = new_node
        return head
    
    def printList(self, head):
        current = head

        while current:
            print(current.data, end=' ')
            current = current.next
        print()

class Solution:
    def reverseList(self, node):
        prev = None
        current = node

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def addOne(self, head):
        head = self.reverseList(head)

        current = head
        carry = 1

        while current and carry:
            sum_ = current.data + carry
            current.data = sum_ % 10
            carry = sum_ // 10

            if not current.next and carry:
                current.next = Node(carry)
                carry = 0
            current = current.next
        
        head = self.reverseList(head)
        return head
    
if __name__ == "__main__":
    head = None
    ll = LinkedList()
    sol = Solution()

    # Example: Number 129 (1 -> 2 -> 9)
    head = ll.append(head, 1)
    head = ll.append(head, 2)
    head = ll.append(head, 9)

    print("Original Number: ", end='')
    ll.printList(head)

    head = sol.addOne(head)

    print("After Adding One: ", end='')
    ll.printList(head)