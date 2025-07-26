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

    def delete_kth(self, head, k):
        if head is None:
            return None

        if k == 1:
            return head.next  # Remove the head

        temp = head
        count = 1

        while temp and count < k - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            return head

        temp.next = temp.next.next

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
new_head = l1.delete_kth(l1.head, 3)
print("After Removing kth:")
l1.printLL(new_head)
