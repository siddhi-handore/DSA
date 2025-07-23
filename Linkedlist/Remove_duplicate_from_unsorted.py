# Optimal Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def printLL(self, head):
        temp = head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

    def removeDup(self, head):
        if head is None or head.next is None:
            return head

        seen = set()
        curr = head
        prev = None
        while curr:
            if curr.data in seen:
                prev.next = curr.next
                curr = curr.next
            else:
                seen.add(curr.data)
                prev = curr
                curr = curr.next
        return head


l1 = LinkedList()
l1.append(5)
l1.append(7)
l1.append(20)
l1.append(5)
l1.append(7)
print("Original Linked List:")
l1.printLL(l1.head)
new_head = l1.removeDup(l1.head)
print("After Removing Duplicates:")
l1.printLL(new_head)
