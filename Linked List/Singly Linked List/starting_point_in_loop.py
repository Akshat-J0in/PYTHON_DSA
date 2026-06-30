class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class solution:
    def starting_point(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next

            if slow == fast:
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

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
    starting_val = sol.starting_point(head)

    print(starting_val.data)