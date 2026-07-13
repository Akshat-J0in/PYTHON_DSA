class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def insert_node(self, head, val):
        new_node = Node(val)

        if head[0] is None:
            head[0] = new_node
            return
        
        temp = head[0]
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp
    
    def print_DLL(self, head):
        temp = head

        while temp:
            print(temp.data, end = ' ')
            if temp.next:
                print('<->', end=' ')
            temp = temp.next
        print()
    
    def delete_target_node(self, head, target):
        current = head

        while current:
            next_node = current.next

            if current.data == target:
                if current.prev:
                    current.prev.next = current.next
                else:
                    head = current.next

                if current.next:
                    current.next.prev = current.prev
            
            current = next_node
        
        return head
    
if __name__ == "__main__":
    sol = Solution()
    head = [None]

    sol.insert_node(head,1)
    sol.insert_node(head,2)
    sol.insert_node(head,3)
    sol.insert_node(head,2)
    sol.insert_node(head,4)
    sol.insert_node(head,2)
    sol.insert_node(head,5)

    print("Original List: ")
    sol.print_DLL(head[0])

    target = 2

    head[0] = sol.delete_target_node(head[0], target)

    print("\nAfter deleting value", target, ":")
    sol.print_DLL(head[0])

