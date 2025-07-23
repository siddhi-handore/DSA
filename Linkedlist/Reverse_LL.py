# Striver's approach
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    @staticmethod
    def reverseLL(head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev  

    @staticmethod
    def printLL(head):
        temp = head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)

    print("Original Linked List:")
    LinkedList.printLL(head)

    head = LinkedList.reverseLL(head)

    print("Reversed Linked List:")
    LinkedList.printLL(head)

if __name__ == '__main__':
    main()
