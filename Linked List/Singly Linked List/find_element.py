class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def is_present(self, head, key):
        curr = head
        while curr is not None:
            if curr.data == key:
                return True
            
            curr = curr.next
        return False
                

if __name__ == "__main__":
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)

    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next
    
    obj = solution()

    if obj.is_present(head, 100):
        print("Found")
    else:
        print("Not Found")