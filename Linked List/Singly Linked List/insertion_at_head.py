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