class QueueFullError(Exception):
    def __init__(self, message, errors = None):
        super(QueueFullError, self).__init__(message)

class QueueEmptyError(Exception):
    def __init__(self, message, errors = None):
        super(QueueEmptyError, self).__init__(message)

class Queue:
    def __init__(self, capacity):
        self.arr = [None] * capacity
        self.capacity = capacity
        self.bottom = 0
        self.top = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size >= self.capacity

    def enqueue(self, element):
        if self.is_full():
            raise QueueFullError("Queue is full: cannot enqueue in a full queue")
        self.arr[self.top] = element
        self.top = (self.top + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("Queue is empty: cannot dequeue from an empty queue")
        elem = self.arr[self.bottom]
        self.bottom = (self.bottom + 1) % self.capacity
        self.size -= 1
        return elem


if __name__ == "__main__":
    queue = Queue(15)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    value = queue.dequeue()
    print value
