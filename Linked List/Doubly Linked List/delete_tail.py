class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class solution:
    def delete_tail(self, head):
        if not head:
            return None
        
        if not head.next:
            return None
        
        temp = head
        while temp.next:
            temp = temp.next
        
        temp.prev.next = None

        return head

if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    curr = head
    while curr:
        print(curr.data, end = ' ')
        curr = curr.next
    
    print()

    obj = solution()

    head = obj.delete_tail(head)

    curr = head
    while curr:
        print(curr.data, end = ' ')
        curr = curr.next