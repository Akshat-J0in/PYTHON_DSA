"""
Problem Statement:
Given the head of a linked list, print the length of the linked list.
"""



class node:
    def __init__(self, data1):
        self.data = data1
        self.next = None

class solution:
    def count_length(self, head):
        count = 0
        temp = head
        while temp is not None:
            count +=1
            temp = temp.next
        return count

if __name__ == "__main__":
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)

    obj = solution()
    print(obj.count_length(head))
"""
This is a simple code where we have created a node and then in main we are filling the values.
Then i have created a class where we have a method count_length. Over here we have created a count variable and we run the loop till our head is not null
And till our head is not null, we will increment the count variable.
Once we are out off the loop, we will return the count.
"""