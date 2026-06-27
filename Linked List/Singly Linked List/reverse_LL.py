class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def reverse_LL(self, head):
        prev = None
        curr = head

        while curr:
            front = curr.next

            curr.next = prev
            prev = curr

            curr = front
        return prev

def print_LL(head):
    while head:
        print(head.data, end= " ")
        head = head.next
    print()

head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)

sol = solution()
new_head = sol.reverse_LL(head)
print_LL(new_head)
