# Using Rabbit and tortoise algo
# Time Complexity :O(n)
# (Auxiliary)Space Complexity : O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print(middle(head))

if __name__ == '__main__':
    main()
