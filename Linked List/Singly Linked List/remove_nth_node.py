"""
Problem Statement:
Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.
"""



class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class solution:
    def printLL(self,head):
        while head is not None:
            print(head.data, end = " ")
            head = head.next

    def remove_node(self, head, N):
        dummy = node(0,head)
        slow = dummy
        fast = dummy

        for _ in range(N+1):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    N = 3

    head = node(arr[0])
    head.next = node(arr[1])
    head.next.next = node(arr[2])
    head.next.next.next = node(arr[3])
    head.next.next.next.next = node(arr[4])

    sol = solution()
    head = sol.remove_node(head, N)
    sol.printLL(head)
    