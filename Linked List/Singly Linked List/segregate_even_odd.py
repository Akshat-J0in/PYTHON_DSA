class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class solution:
    def segregateEvenOdd(self, head):
        
        if head is None or head.next is None:
            return head

        evenHead = evenTail = None
        oddHead = oddTail = None

        current = head

        while current:
            if current.data % 2 == 0:
                if not evenHead:
                    evenHead = evenTail = current
                else:
                    evenTail.next = current
                    evenTail = current
            else:
                if not oddHead:
                    oddHead = oddTail = current
                else:
                    oddTail.next = current
                    oddTail = current
            current = current.next
        
        if not evenHead:
            return oddHead
        
        if not oddHead:
            return evenHead
        
        evenTail.next = oddHead
        oddTail.next = None

        return evenHead


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next

if __name__ == '__main__':
    head = node(17)
    head.next = node(15)
    head.next.next = node(8)
    head.next.next.next = node(12)
    head.next.next.next.next = node(10)
    head.next.next.next.next.next = node(5)
    head.next.next.next.next.next.next = node(4)

    sol = solution()
    new_head = sol.segregateEvenOdd(head)
    printList(new_head)