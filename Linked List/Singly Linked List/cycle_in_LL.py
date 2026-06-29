"""
Problem Statement:
Given a Linked List, determine whether the linked list contains a cycle or not.
"""



# Approach 1:
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
"""
Here in this approach, we have used the hash map approch in which we strore the frequency of the element in the hashmap and if we see
a element appearing one more time that is twice we return true that there is a loop in a lined list else retrun false.
"""



# Approach 2:
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

"""
Here we have used the slow and fast pointer approch in which if we have two pointer starting from the first node and then we increment the
slow with next and the fast with next.next and once they both meet, we can say that yes there is a loop otherwise there is no loop.
"""