# class node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next

# class solution:
#     def detect_loop(self, head):
#         temp = head

#         nodeMap = {}

#         while temp is not None:
#             if temp in nodeMap:
#                 return True
            
#             nodeMap[temp] = 1

#             temp = temp.next
        
#         return False

# if __name__ == '__main__':
#     head = node(1)
#     second = node(2)
#     third = node(3)
#     fourth = node(4)
#     fifth = node(5)

#     head.next = second
#     second.next = third
#     third.next = fourth
#     fourth.next = fifth
#     fifth.next = third

#     sol = solution()

#     if sol.detect_loop(head):
#         print("Loop detected")
#     else:
#         print("No loop detected")


class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class solution:
    def detect_loop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        else:
            return False

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

    if sol.detect_loop(head):
        print("Loop detected")
    else:
        print("No loop detected")