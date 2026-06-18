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