class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def convert_list_to_dll(arr):
    head = node(arr[0])

    prev = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        new_node.prev = prev
        prev.next = new_node
        prev = new_node
    return head

def print_dll(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

def reverse_dll(head):
    temp = None
    curr = head

    while curr is not None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        
        curr = curr.prev

    if temp is not None:
        head = temp.prev
    
    return head

if __name__ == "__main__":
    arr = [10,20,30,40,50]

    head = convert_list_to_dll(arr)
    print_dll(head)
    print()
    head = reverse_dll(head)
    print_dll(head)