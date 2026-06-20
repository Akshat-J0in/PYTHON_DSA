class node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

arr = [2,5,8,7]

head = node(arr[0])

prev = head

for i in range(1, len(arr)):
    temp = node(arr[i],None,prev)
    prev.next = temp
    prev = temp

while head:
    print(head.data, end=' ')
    head = head.next