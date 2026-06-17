"""
Problem statement:
Given a linked list and an integer value val,
insert a new node with that value at the beginning (before the head) of the list
and return the updated linked list.
"""



class node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1

class solution:
    def insert_new_head(self, head, new_data):
        new_node = node(new_data, head)
        return new_node

if __name__ == "__main__":
    head = node(2)
    head.next = node(3)

    print("List before inserting a new head")

    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next

    sol = solution()

    head = sol.insert_new_head(head, 1)

    print()
    print("List after adding a new head")
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
"""
Over here i have first created a class for node where we initialize th elinked list.
Then i have created a class solution where we have created a new method in which we are taking two parameter as input
one is the head of the LL and the other is the new value that will become the head.
Now we again create a noe in that method where the new node is pointing to the head of the prev LL head.
and then we print the LL.
"""