class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class solution:

    def delete_middle(self, head):

        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head.next.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return head

    def printLL(self, head):  
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == '__main__':
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)

    sol = solution()
    sol.printLL(head)

    print()

    head = sol.delete_middle(head)

    sol.printLL(head)