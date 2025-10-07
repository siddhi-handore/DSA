
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def startNode(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        slow = self.head
        while slow != fast:
            slow = slow.next
        return slow.data

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def createLoop(self, pos1, pos2):
        start = self.head
        end = self.head
        i = 1
        while start and i < pos1:
            start = start.next
            i+=1
        i = 1
        while end and i < pos2:
            end = end.next
            i+=1
        end.next = start

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")




