class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class solution:
    def length_of_LL(self, head):
        slow = head
        fast = head

        count = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count += 1
                slow = slow.next

                while slow != fast:
                    count += 1
                    slow = slow.next
                
                return count
        return 0
    

if __name__ == '__main__':
    head = node(1)
    second = node(2)
    third = node(3)
    fourth = node(4)
    fifth = node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = third

    sol = solution()
    length = sol.length_of_LL(head)
    print(length)