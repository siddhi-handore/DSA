# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def printLL(self, head):
        temp = head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def find_pairs(self, head, tot):
        left = head
        right = find_tail(head)
        pairs = []
        while left.data < right.data:
            if left.data + right.data == tot:
                pairs.append([left.data, right.data])
                left = left.next
                right = right.prev
            elif left.data + right.data < tot:
                left = left.next
            else:
                right = right.prev
        return pairs


def find_tail(head):
    temp = head
    while temp.next:
        temp = temp.next
    return temp

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(9)
print("Original Linked List:")
l1.printLL(l1.head)
pair = l1.find_pairs(l1.head, 5)
print(pair)
