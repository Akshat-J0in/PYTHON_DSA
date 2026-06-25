class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

def find_middle(head):

    slow = head
    fast = head

    while fast and fast.next and slow:
        fast = fast.next.next

        slow = slow.next
    
    return slow

if __name__ == '__main__':
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
    head.next.next.next.next = node(5)

    middle_element = find_middle(head)

    print("the middle element is: ", middle_element.data)