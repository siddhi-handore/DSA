# Enqueue: Adds new elements to the end of the queue. Checks if the queue has space
# before insertion, then increments the size.
# Dequeue: Removes the front element by shifting all remaining elements one
# position to the left. Decrements the queue size after removal.
# getFront: Returns the first element of the queue if it's not empty.
# Returns -1 if the queue is empty.
# Display: Iterates through the queue from the front to the current size
# and prints each element.

class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        if len(self.q) == 0:
            return True
        return False

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        if not self.is_empty():
            return self.q.pop(0)

    def front(self):
        if not self.is_empty():
            return self.q[0]
        return None

    def display(self):
        for i in self.q:
            print(i, end=" ")

q = Queue()
q.enqueue(4)
q.enqueue(2)
q.enqueue(8)
q.enqueue(7)
q.enqueue(10)
q.enqueue(15)
print("Queue")
q.display()
print(f"Queue front: {q.front()}")
print(f"Remove front: {q.dequeue()}")
q.display()