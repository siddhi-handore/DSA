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

    def del_occurences(self, head, key):
        temp = head
        while temp:
            if temp.data == key:
                if temp == head:
                     head = head.next
                next_node = temp.next
                prev_node = temp.prev

                if next_node:
                    next_node.prev = prev_node
                if prev_node:
                    prev_node.next = next_node
                temp = next_node
            else:
                temp = temp.next
        return head



l1 = LinkedList()
l1.append(10)
l1.append(4)
l1.append(10)
l1.append(10)
l1.append(6)
l1.append(10)
print("Original Linked List:")
l1.printLL(l1.head)
new_head = l1.del_occurences(l1.head, 10)
print("After Removing occurences:")
l1.printLL(new_head)
