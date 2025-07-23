# Floyd's linked list Cycle Detection algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    @staticmethod
    def Detect(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

def main():
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = head.next

    print(LinkedList.Detect(head))

if __name__ == '__main__':
    main()