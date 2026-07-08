"""
Problem Statement:
Given a linked list containing only 0's, 1's, and 2's, sort the linked list by rearranging the links (not by changing the data values).
"""



class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class solution:
    def sortLL(self,head):
        zero_dummy = node(-1)
        one_dummy = node(-1)
        two_dummy = node(-1)

        zero_tail = zero_dummy
        one_tail = one_dummy
        two_tail = two_dummy

        curr = head

        while curr:
            if curr.data == 0:
                zero_tail.next = curr
                zero_tail = zero_tail.next
            elif curr.data == 1:
                one_tail.next = curr
                one_tail = one_tail.next
            else:
                two_tail.next = curr
                two_tail = two_tail.next
            
            curr = curr.next
        
        zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next
        one_tail.next = two_dummy.next
        two_tail.next = None

        return zero_dummy.next

def printLL(head):
    temp = head

    while temp:
        print(temp.data, end=" ")
        temp = temp.next

if __name__ == '__main__':
    head = node(1)
    head.next = node(2)
    head.next.next = node(0)
    head.next.next.next = node(1)
    head.next.next.next.next = node(2)
    head.next.next.next.next.next = node(0)

    printLL(head)

    sol = solution()
    new_ll = sol.sortLL(head)
    print()

    printLL(new_ll)

